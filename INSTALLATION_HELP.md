# 🪟 Windows Installation Guide

Complete step-by-step guide for installing and running the AI Content Summarizer on Windows.

---

## Prerequisites

### 1. Python Installation

**Check if Python is installed:**
1. Open Command Prompt (Win + R, type `cmd`)
2. Type: `python --version`
3. Should show Python 3.8 or higher

**If Python is NOT installed:**

1. Download Python from https://www.python.org/downloads/
2. Click "Download Python 3.11" (or latest)
3. **IMPORTANT:** Check "Add Python to PATH"
4. Click "Install Now"
5. Wait for installation to complete
6. Verify: Open cmd, type `python --version`

### 2. Git Installation (Optional but Recommended)

1. Download from https://git-scm.com/download/win
2. Run installer, keep default settings
3. Click "Install"

---

## Installation Steps

### Step 1: Get the Project

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/yourusername/AI-powered-content-summarizer.git
cd AI-powered-content-summarizer
```

**Option B: Manual Download**
1. Go to GitHub repository
2. Click "Code" (green button)
3. Click "Download ZIP"
4. Extract ZIP file
5. Open extracted folder

### Step 2: Open Command Prompt in Project Folder

1. Navigate to project folder in File Explorer
2. Click address bar, clear it
3. Type: `cmd`
4. Press Enter
5. Command Prompt opens in project folder

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

⏳ Wait 1-2 minutes for environment creation

### Step 4: Activate Virtual Environment

```bash
venv\Scripts\activate
```

✅ You should see `(venv)` at the start of each line in Command Prompt

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

⏳ **First installation takes 10-15 minutes** (downloading AI models)

**Progress indicators:**
- `Collecting transformers` → Normal
- `Downloading model` → Normal (3-5GB download)
- `Successfully installed` → Done!

### Step 6: Run the Application

```bash
streamlit run streamlit_app.py
```

✅ Application opens at: `http://localhost:8501`

---

## Troubleshooting for Windows

### Issue: "Python is not recognized"

**Cause:** Python not in PATH

**Solution:**
1. Uninstall Python (Settings → Apps → Uninstall)
2. Reinstall and **CHECK "Add Python to PATH"**
3. Restart Command Prompt
4. Try again

### Issue: "venv\Scripts\activate" doesn't work

**Cause:** PowerShell execution policy

**Solution:**
1. Open PowerShell as Administrator
2. Type: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Type: `Y` and press Enter
4. Try again

**Alternative:** Use Command Prompt (cmd) instead of PowerShell

### Issue: "pip: command not found"

**Solution:**
```bash
python -m pip install -r requirements.txt
```

### Issue: "port 8501 is already in use"

**Solution:**
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Issue: Installation hangs or takes too long

**Solution:**
```bash
# Cancel (Ctrl + C)
# Try again with verbose mode
pip install -r requirements.txt -v
```

### Issue: "Memory error" during model download

**Solution:**
1. Close other applications
2. Free up disk space (need ~5GB)
3. Try installation again

### Issue: App shows "resource unavailable"

**Solution:**
1. Close all Command Prompts
2. Open new Command Prompt
3. Navigate to project folder
4. Activate venv: `venv\Scripts\activate`
5. Run app: `streamlit run streamlit_app.py`

---

## Common Command Prompt Issues

### Changing Directories

```bash
# Change drive (if project is on D:\)
D:

# Navigate to project folder
cd OneDrive\Documents\AI-powered-content-summarizer

# Go up one level
cd ..

# Go to home directory
cd %USERPROFILE%
```

### Viewing Files

```bash
# List files in current folder
dir

# List files with details
dir /s
```

### Clearing Screen

```bash
cls
```

---

## First Run Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] App runs at localhost:8501
- [ ] Text input works
- [ ] Model loads successfully
- [ ] Summary generates

---

## Testing the Installation

### Test 1: Quick Test
```bash
# In Command Prompt with venv activated
streamlit run streamlit_app.py
```

1. App opens in browser
2. Type sample text
3. Click "🚀 Generate Summary"
4. Summary appears

### Test 2: All Features
- [ ] Text input works
- [ ] Copy button works
- [ ] Download button works
- [ ] History saves

### Test 3: Different Models
- [ ] BART model loads
- [ ] PEGASUS model loads
- [ ] T5 model loads
- [ ] DistilBART model loads

---

## Development Setup (Optional)

**If you want to contribute or develop:**

```bash
# Install development tools
pip install -r requirements-dev.txt

# Format code
black streamlit_app.py utils.py

# Check code quality
flake8 streamlit_app.py utils.py

# Run tests
pytest

# Type checking
mypy streamlit_app.py
```

---

## Updating the Project

### Update from GitHub

```bash
# Make sure venv is activated
venv\Scripts\activate

# Pull latest changes
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt
```

### Restart App

```bash
# Kill current process (Ctrl + C)
# Run again
streamlit run streamlit_app.py
```

---

## Deploying to Streamlit Cloud

**Before deployment:**
1. Push code to GitHub
2. Follow [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. Share your deployed URL!

---

## Useful Windows Shortcuts

| Shortcut | Action |
|----------|--------|
| Win + R | Open Run dialog |
| Win + E | Open File Explorer |
| Ctrl + C | Stop current command |
| Ctrl + Shift + Delete | Clear browsing data |
| Alt + F4 | Close window |

---

## Command Reference

| Command | Purpose |
|---------|---------|
| `python --version` | Check Python version |
| `pip --version` | Check pip version |
| `python -m venv venv` | Create virtual environment |
| `venv\Scripts\activate` | Activate virtual environment |
| `deactivate` | Deactivate virtual environment |
| `pip install -r requirements.txt` | Install dependencies |
| `streamlit run streamlit_app.py` | Run application |
| `pip list` | Show installed packages |
| `pip install package-name` | Install specific package |
| `pip uninstall package-name` | Uninstall package |

---

## Performance Tips for Windows

1. **Close Unnecessary Apps**
   - Models need 3-4GB RAM
   - Close browser tabs, heavy apps

2. **Disable Sleep Mode**
   - Settings → Power & sleep → Screen: Never
   - This prevents interruptions

3. **Increase Virtual Memory** (if RAM low)
   - Settings → System → Advanced System Settings
   - Performance → Virtual Memory
   - Increase to 8GB

4. **Use SSD**
   - Installation faster on SSD
   - C: drive preferred

---

## Getting More Help

### When Something Goes Wrong

1. **Read the error message carefully**
   - Most errors have solutions in messages

2. **Try these steps:**
   - Restart Command Prompt
   - Close and reopen app
   - Clear cache: `streamlit cache clear`
   - Restart computer

3. **Check resources:**
   - README.md - Full documentation
   - QUICK_START.md - Quick guide
   - DEPLOYMENT_GUIDE.md - Deploy info

4. **Get help:**
   - GitHub Issues
   - Streamlit Discord
   - Stack Overflow

---

## Success! 🎉

If you've completed all steps, the app is now running!

1. Open browser: `http://localhost:8501`
2. Try the app
3. Test different models
4. Download or copy results
5. Deploy to Streamlit Cloud

**Next steps:**
- Read [README.md](README.md) for full features
- Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) to deploy online
- Visit [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) to contribute

---

## Quick Reference: From Start to App Running

```bash
# 1. Navigate to project folder (in Command Prompt)
cd path\to\AI-powered-content-summarizer

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install everything
pip install -r requirements.txt

# 5. Run the app
streamlit run streamlit_app.py

# 6. Open browser to localhost:8501
# 🎉 Done!
```

---

**Happy summarizing! 📝✨**

For more help, see other documentation files or visit https://docs.streamlit.io
