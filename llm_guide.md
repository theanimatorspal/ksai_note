# Project Name
habit_tracker

# Project Purpose
Recently I have read atomic habits so I want to create a personal habit tracker for myself.

# Technologies and Code of Conduct
- python 
    - fastapi and uvicorn
- html (You can use as modern features as you want to make it better)
- js (You can use as modern features as you want, use proper libraries if the thing is already present in any library)
- css (Don't ever hardcode anything in pixels, use proper libraries if the thing is already present in any library, make the colors contrasting so that it is easy on the eyes, should be dark mode. Do proper animations, exoctic animations make it super cool.)
- polars + parquet file (Use this file based to do everything, saving, loading and stuff like that)
(You should not write any comments in code, ZERO comments, and write very small variable names to save token size for LLMs, very small names but understandable, like dt for date)

# Folder Structure (Initial)
- index.html which should contain all html css and js
- main.py
- requirements.txt

# Features
- This is entirely personal project, NO COLLABORATION is intended in any way
- The CSS should be very beautiful and dark themed
- If I open the browser in the fastapi url:port thing then it should have a loading screen (if it is loading database from the file)
- When it is loaded, It should have a very big table (not actually table but card based designed row and columns) in which
    - For each BIG ROW (representing each day)
        - Left Most side should be date
        - And then A Big Column will be there which is "Tasks", this will have
            - A Timer (interactive, If I press it it will start from 0:00, and count minutes, seconds and hours and if I press again it will pause, If I do ctrl shift alt click then it will reset to 0:00 each of the tasks should have this, if I reset it then the task should be automatically deleted.), BTW the timer should run in backed for each task, if I close the browser then it should still be on in the background.
            - A Traffic light style thing that will toggle if I select it from green, gray and red (should also be the same color for the timer, and if timer is increasing for good habit then it should be more greener and greener, and redder and redder for bad habit, start with very light shades (you can gamify by making good sounds every 5-10 minutes to keep me motivated for good habit and bad sounds every 2-3 minutes to keep me demotivated for bad habit.), for neutral habit don't do anything.), which will represent good, neutral and bad habit.
            - A label (editable) Habit name
            - [Add Task] Button that will add task and append (not prepend) it there.
        - Then third would be "Thoughts" It should have a richtext markdown editor kinda thing, while engaged in habit, I will write thoughts there and maybe like discussions (THIS SHOULD be subject to EACH of the tasks)
        - At the bottom right there should be small button that will export to markdown (today's details).
- If today is the new day since the database updated then automatically add one cell (I mean the big row) PREPEND to the existing rows, and I track my habits there.
- Every change that happens to the UI should be properly tracked (maybe poll each 10 seconds if any change is there, and also do like if timer started happens for any habit then you can add that).
- Design this such that this would run 24x7. 
- Anything that is of previous day should not be able to be changed but should be able to view it (the other big rows), You should make it viewable but not editable.   

