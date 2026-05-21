# 🚀 Quick Start Guide

Get the AI Content Summarizer running in 5 minutes!

---

## Option 1: Try Online (Easiest)

**No installation needed!**

1. Click this link: [AI Content Summarizer App](https://summarizer.streamlit.app)
2. Select input method (Text, PDF, or URL)
3. Paste your content
4. Click "Generate Summary"
5. Done! ✅

---

## Option 2: Run Locally (Windows/Mac/Linux)

### 1. Check Python Installation
```bash
python --version
# Should be 3.8 or higher
```

If Python is not installed, download from https://www.python.org

### 2. Download Project

**Option A: Using Git**
```bash
git clone https://github.com/yourusername/AI-powered-content-summarizer.git
cd AI-powered-content-summarizer
```

**Option B: Download ZIP**
1. Visit GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal in extracted folder

### 3. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

⏳ **First time installation might take 5-10 minutes** (downloading AI models)

### 5. Run the App
```bash
streamlit run streamlit_app.py
```

✅ **App opens at:** http://localhost:8501

---

## Usage

### Summarize Text
1. Select "Text" tab
2. Paste content (minimum 50 characters)
3. Adjust settings if needed:
   - Choose model (top left)
   - Select summary length
4. Click "🚀 Generate Summary"
5. Download or copy results

### Summarize PDF
1. Select "PDF" tab
2. Upload a PDF file
3. Process automatically
4. Choose summary settings
5. Click "🚀 Generate Summary"

### Summarize Website
1. Select "URL" tab
2. Paste a website URL
3. Click to fetch content
4. Choose summary settings
5. Click "🚀 Generate Summary"

---

## Model Recommendations

| Use Case | Model | Speed |
|----------|-------|-------|
| Quick summaries | DistilBART | ⚡⚡⚡ |
| General text | BART (Default) | ⚡⚡ |
| News articles | PEGASUS | ⚡⚡ |
| Special topics | T5 | ⚡⚡ |

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl + Enter` | Generate summary |
| `Ctrl + C` | Copy summary |
| `R` | Refresh page |

---

## Troubleshooting

### "Module not found" Error
```bash
pip install -r requirements.txt
```

### "Port 8501 already in use"
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Slow on First Run
- First launch downloads AI models (~2GB)
- Subsequent runs are instant (cached)
- Be patient ⏳

### App Not Opening
```bash
# Try with verbose output
streamlit run streamlit_app.py --logger.level=debug
```

---

## Next Steps

1. ✅ Try the online version: https://summarizer.streamlit.app
2. ✅ Test with different content types
3. ✅ Experiment with different models
4. ✅ Deploy your own version:
   - See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## Features Overview

- ✅ Text input
- ✅ PDF upload & processing
- ✅ URL fetching & extraction
- ✅ Multiple AI models
- ✅ Adjustable summary lengths
- ✅ Download summaries
- ✅ Summary history
- ✅ Statistics & metrics
- ✅ Modern UI
- ✅ Copy to clipboard

---

## System Requirements

| Component | Requirement |
|-----------|-------------|
| Python | 3.8+ |
| RAM | 4GB+ |
| Disk | 3GB+ (for models) |
| Internet | Required (first run) |
| OS | Windows, Mac, Linux |

---

## Getting Help

1. **README.md** - Full documentation
2. **DEPLOYMENT_GUIDE.md** - Deploy instructions
3. **GitHub Issues** - Report bugs
4. **Streamlit Docs** - https://docs.streamlit.io

---

## Key Files

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Main application |
| `utils.py` | Helper functions |
| `requirements.txt` | Dependencies |
| `README.md` | Full documentation |
| `DEPLOYMENT_GUIDE.md` | Deploy to cloud |

---

**Ready to start? Run:**
```bash
streamlit run streamlit_app.py
```

**Or visit:** https://summarizer.streamlit.app

---

Made with ❤️ using Python & Streamlit
