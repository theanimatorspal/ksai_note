<h1 align="center">📓 ksai_note</h1>
<p align="center"><i>Your Infinitely Nestable, Local-First, Browser-Based Digital Whiteboard</i></p>
<p align="center"><b>Built with:</b> HTML5, Vanilla JS (ESM) 🍦 | Excalidraw, D3.js, Marked.js 🛠️ | IndexedDB 🗄️</p>
<p align="center">
  <img src="https://img.shields.io/badge/storage-IndexedDB powered-blue?style=flat-square&logo=databricks" />
  <img src="https://img.shields.io/badge/dependencies-creatively abused-orange?style=flat-square&logo=javascript" />
  <img src="https://img.shields.io/badge/UI-aggressively dark-black?style=flat-square&logo=visualstudiocode" />
  <img src="https://img.shields.io/badge/features-surprisingly complete-green?style=flat-square&logo=readme" />
  <img src="https://img.shields.io/badge/export-actually works-brightgreen?style=flat-square&logo=html5" />
  <img src="https://img.shields.io/badge/backend-doesn't exist-critical?style=flat-square&logo=icloud" />
</p>

---

## 📡 About

**ksai\_note** is a deceptively powerful note-taking application that lives entirely in a **single HTML file**. It combines the infinite canvas of **Excalidraw** with a robust notebook organization system, all running locally in your browser. No servers, no sign-ups, no cloud—just your notes, stored securely and privately in your browser's IndexedDB.

It's the love child of a digital whiteboard and a nested notebook, designed for developers, students, and anyone who thinks better visually.

> ✨ Zero installation, 100% browser-based.
> 💾 All data is saved locally. If you clear your browser data, it's gone!

---

## 🔬 Core Features

| Feature                    | Status              | Notes                                                                    |
| -------------------------- | ------------------- | ------------------------------------------------------------------------ |
| Excalidraw Canvas          | ✅ Fully Integrated | The infinite, vector-based whiteboard is your page.                      |
| Notebook Hierarchy         | ✅ Supported        | Nest sections and subsections to your heart's content.                   |
| Local-First Storage        | 🗄️ IndexedDB      | Fast, private, and works completely offline.                             |
| Math Equation Plotter      | 🧠 Functional       | Plot `y = sin(x) * 50` directly onto the canvas using D3.js.             |
| Markdown-to-Canvas         | 📝 Supported        | Render Markdown, including code blocks, as native drawing elements.      |
| Self-Contained HTML Export | 📤 `.html`          | Export an entire notebook as a single, interactive, viewable HTML file.  |
| Backup & Share             | 💾 `.ksai_note`     | Import/Export notebooks using a custom file format for easy backups.     |
| Plugin Toolbar             | 🔌 Included         | A simple, extendable toolbar for adding new tools like the plugins above.|

---

## 🖼️ Screenshot Gallery

*(Add your own screenshots here!)*

### Main Interface (Dark Mode is not optional, it's a feature)

<img src="https://user-images.githubusercontent.com/username/repo/assets/placeholder1.png" width="100%" alt="A screenshot of the main UI showing the sidebar with nested notebooks and the Excalidraw canvas.">

---

### Plugins in Action (Math Plotter & Markdown Renderer)

<img src="https://user-images.githubusercontent.com/username/repo/assets/placeholder2.png" width="100%" alt="A screenshot showing a math plot and a rendered Markdown table on the canvas.">

---

## 🚀 How to Use

This is the best part. There is **no build process**.

1.  Download the `ksai_note.html` file from this repository.
2.  Open it in a modern web browser (like Chrome, Firefox, or Edge).
3.  That's it. Start creating.

```bash
# No, seriously. Just open the HTML file.
# You don't need to run this. It's just for show.
open ./ksai_note.html
