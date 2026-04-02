# 📖 LexiRead — PDF Reader with Vocabulary Lookup

Read PDFs and look up any word instantly from vocabulary.com — without leaving the page.

---

## ✨ Features

- Open any PDF and read it page by page
- Select any word → click **Look Up** → see its meaning in the side panel
- Pulls rich definitions from vocabulary.com (short blurb, long description, senses + examples)
- Word lookup history for quick re-lookup
- Keyboard shortcuts: `←` / `→` to change pages, `Enter` to look up selected word

---

## 🚀 Setup (One Time)

### 1. Make sure Python is installed
```bash
python --version   # should be 3.7+
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python app.py
```

Then open your browser and go to:
```
http://localhost:5000
```

That's it! The app will open in your browser.

---

## 📂 Project Structure

```
vocab_reader/
├── app.py              ← Flask backend (scrapes vocabulary.com)
├── requirements.txt    ← Python dependencies
├── README.md
└── static/
    └── index.html      ← The full frontend app
```

---

## 🔍 How It Works

1. You open a PDF in the browser using the built-in PDF.js reader
2. Select any word with your mouse
3. A **Look Up** button pops up near your selection
4. The frontend asks the Flask backend: `/lookup?word=emblazon`
5. Flask fetches vocabulary.com and extracts the definition from the page's metadata and HTML
6. The definition appears in the right-hand panel — without you ever leaving the reader

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` | Previous page |
| `→` | Next page |
| `Enter` | Look up selected word (when tooltip is visible) |
