from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import polars as pl
import os
from datetime import datetime, date
from typing import Dict, List, Optional
from pydantic import BaseModel
import json
import time

app = FastAPI()

class Task(BaseModel):
    id: str
    nm: str
    tp: str
    tm: int
    st: Optional[int] = None

class Thought(BaseModel):
    tk_id: str
    ct: str

class DayData(BaseModel):
    dt: str
    tsks: List[Task]
    ths: List[Thought]

DB_FILE = "hb.parquet"

def get_db():
    if not os.path.exists(DB_FILE):
        df = pl.DataFrame({
            "dt": [],
            "data": []
        }, schema={"dt": pl.Date, "data": pl.Utf8})
        df.write_parquet(DB_FILE)
        return df
    return pl.read_parquet(DB_FILE)

def save_db(df):
    df.write_parquet(DB_FILE)

def get_today_str():
    return date.today().isoformat()

@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("index.html")

@app.get("/api/data")
async def get_data():
    time.sleep(1)
    df = get_db()
    tdy = get_today_str()
    
    if df.height == 0 or tdy not in df["dt"].to_list():
        new_row = pl.DataFrame({
            "dt": [date.fromisoformat(tdy)],
            "data": [json.dumps({"tsks": [], "ths": []})]
        })
        if df.height == 0:
            df = new_row
        else:
            df = pl.concat([new_row, df])
        save_db(df)
    
    result = []
    for row in df.iter_rows(named=True):
        dt_str = row["dt"].isoformat()
        data = json.loads(row["data"])
        result.append({
            "dt": dt_str,
            "tsks": data.get("tsks", []),
            "ths": data.get("ths", []),
            "ed": dt_str == tdy
        })
    
    return result

@app.post("/api/save")
async def save_data(day_data: DayData):
    df = get_db()
    dt_obj = date.fromisoformat(day_data.dt)
    
    data_json = json.dumps({
        "tsks": [t.dict() for t in day_data.tsks],
        "ths": [th.dict() for th in day_data.ths]
    })
    
    mask = df["dt"] == dt_obj
    if mask.sum() > 0:
        df = df.with_columns(
            pl.when(pl.col("dt") == dt_obj)
            .then(pl.lit(data_json))
            .otherwise(pl.col("data"))
            .alias("data")
        )
    else:
        new_row = pl.DataFrame({
            "dt": [dt_obj],
            "data": [data_json]
        })
        df = pl.concat([new_row, df])
    
    save_db(df)
    return {"status": "ok"}

@app.get("/api/export/{dt}")
async def export_md(dt: str):
    df = get_db()
    dt_obj = date.fromisoformat(dt)
    
    row = df.filter(pl.col("dt") == dt_obj)
    if row.height == 0:
        raise HTTPException(404, "Date not found")
    
    data = json.loads(row["data"][0])
    
    md = f"# Habit Tracker - {dt}\n\n"
    
    if data.get("tsks"):
        md += "## Tasks\n\n"
        for tsk in data["tsks"]:
            hrs = tsk["tm"] // 3600
            mins = (tsk["tm"] % 3600) // 60
            secs = tsk["tm"] % 60
            tm_str = f"{hrs:02d}:{mins:02d}:{secs:02d}"
            tp_emoji = {"good": "🟢", "neutral": "⚪", "bad": "🔴"}.get(tsk["tp"], "⚪")
            md += f"- **{tsk['nm']}** {tp_emoji} - Time: {tm_str}\n"
    
    if data.get("ths"):
        md += "\n## Thoughts\n\n"
        for th in data["ths"]:
            md += f"### Task: {th['tk_id']}\n{th['ct']}\n\n"
    
    return {"md": md}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)