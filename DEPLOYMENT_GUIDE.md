# 🚀 Deployment Guide - Streamlit Cloud

This guide provides detailed step-by-step instructions to deploy the AI Content Summarizer to Streamlit Cloud.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [GitHub Setup](#github-setup)
3. [Streamlit Cloud Deployment](#streamlit-cloud-deployment)
4. [Post-Deployment Configuration](#post-deployment-configuration)
5. [Troubleshooting](#troubleshooting)
6. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Prerequisites

Before you begin, ensure you have:

### 1. GitHub Account
- Create a free account at https://github.com
- Verify your email

### 2. Streamlit Community Cloud Account
- Go to https://share.streamlit.io
- Click "Sign up with GitHub"
- Authorize Streamlit to access your GitHub account

### 3. Required Files in Repository
- `streamlit_app.py` (main application)
- `utils.py` (utilities)
- `requirements.txt` (dependencies)
- `.streamlit/config.toml` (configuration)
- `.gitignore` (git ignore rules)
- `README.md` (documentation)

---

## GitHub Setup

### Step 1: Create GitHub Repository

1. **Log in to GitHub**
   - Go to https://github.com and sign in

2. **Create New Repository**
   - Click "+" icon (top right) → "New repository"
   - Repository name: `AI-powered-content-summarizer`
   - Description: "AI-powered Content Summarizer using Streamlit and Transformers"
   - Choose public (for free deployment)
   - Check "Add a README file"
   - Add .gitignore: select "Python"
   - Click "Create repository"

### Step 2: Prepare Your Local Files

1. **Organize Project Files**
```
AI-powered-content-summarizer/
├── streamlit_app.py
├── utils.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── .gitignore
├── README.md
└── LICENSE
```

2. **Verify Key Files**
   - Ensure `streamlit_app.py` is in the root directory (not in a subdirectory)
   - Check `.streamlit/config.toml` exists
   - Confirm `requirements.txt` has all dependencies

### Step 3: Initialize and Push to GitHub

1. **Open Command Prompt/Terminal** in your project directory

2. **Initialize Git Repository**
```bash
git init
```

3. **Add All Files**
```bash
git add .
```

4. **Create Initial Commit**
```bash
git commit -m "Initial commit: AI Content Summarizer application"
```

5. **Connect to GitHub Repository**
   - Go to your GitHub repository
   - Click "Code" button (green)
   - Copy HTTPS URL (e.g., https://github.com/yourusername/AI-powered-content-summarizer.git)
   - In terminal, run:
```bash
git remote add origin https://github.com/yourusername/AI-powered-content-summarizer.git
```

6. **Rename Branch and Push**
```bash
git branch -M main
git push -u origin main
```

7. **Verify on GitHub**
   - Refresh GitHub page
   - Your files should appear in the repository

---

## Streamlit Cloud Deployment

### Step 1: Access Streamlit Cloud

1. **Open Streamlit Cloud**
   - Navigate to https://share.streamlit.io
   - Click "Sign up with GitHub" if not already signed in
   - Or if already signed in, proceed to step 2

### Step 2: Deploy Application

1. **Click "New app" Button**
   - Located in the top left corner

2. **Select Repository**
   - GitHub Account: Select your account
   - Repository: `AI-powered-content-summarizer`
   - Branch: `main`

3. **Configure Main File**
   - Main file path: `streamlit_app.py`
   - This must match your main Streamlit file name

4. **Click "Deploy"**
   - Application deployment will start
   - First deployment takes 2-5 minutes

### Step 3: Monitor Deployment

1. **Watch Deployment Logs**
   - Real-time logs appear in the deployment console
   - Look for "Successfully installed all dependencies"
   - Final message: "App is running"

2. **Common First Deployment Tasks**
   - Downloading models (can take 3-5 minutes)
   - Installing dependencies
   - Initializing Streamlit

3. **Access Your App**
   - Once deployed, you'll see a URL like:
   - `https://yourusername-summarizer.streamlit.app`
   - Bookmark this URL

---

## Post-Deployment Configuration

### Step 1: Test Application

1. **Test All Input Methods**
   - Text input with sample text
   - PDF upload (if available)
   - URL processing

2. **Test All Models**
   - Switch between different models
   - Verify each model loads correctly

3. **Test Features**
   - Summary generation
   - Download functionality
   - History management

### Step 2: Custom Domain (Optional)

1. **Add Custom Domain**
   - Go to app settings (⋮ menu)
   - Select "Settings"
   - Add your custom domain (requires DNS configuration)

### Step 3: Environment Variables (If Needed)

1. **Add Secrets** (for API keys, etc.)
   - Click "⋮" menu → "Settings"
   - Select "Secrets"
   - Add any required environment variables

### Step 4: Share Your App

1. **Copy URL**
   - Format: `https://yourusername-summarizer.streamlit.app`

2. **Share Options**
   - Direct URL sharing
   - Social media (LinkedIn, Twitter)
   - Email to colleagues
   - Include in portfolio

3. **Create Badge** (Optional)
   ```markdown
   [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://yourusername-summarizer.streamlit.app)
   ```

---

## Troubleshooting

### Issue: "Module not found" Error

**Cause:** Missing dependency in `requirements.txt`

**Solution:**
1. Update `requirements.txt` locally
2. Test with `pip install -r requirements.txt`
3. Commit and push to GitHub
4. Click "Rerun" in Streamlit Cloud

```bash
# Local test
pip install -r requirements.txt
streamlit run streamlit_app.py

# Then push
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

### Issue: "Model download timeout"

**Cause:** First model download takes too long

**Solution:**
- Streamlit Cloud will download models on first run
- This can take 5-15 minutes
- Subsequent runs are cached
- Be patient on first deployment

**Alternative:** Pre-download models
1. Modify `utils.py` to use lighter model by default
2. Or wait and let it download on first user access

### Issue: "Memory exceeded"

**Cause:** Model too large for available memory

**Solution:**
- Use lighter model: `distilbart-cnn-6-6`
- Reduce text input size
- Streamlit Cloud provides sufficient memory for most models

Edit `utils.py`:
```python
# Default lighter model
AVAILABLE_MODELS = {
    "distilbart-cnn-6-6": "DistilBART (Lightweight)",
    # ... other models
}
```

### Issue: "App not responding"

**Cause:** Server overload or long processing time

**Solution:**
- Model inference can take 10-30 seconds
- Click "Always rerun" in Streamlit Cloud settings if stuck
- Refresh page and try again

### Issue: "Deploy button shows 'Update available'"

**Cause:** New changes pushed to GitHub

**Solution:**
- Streamlit Cloud automatically detects changes
- Click "Rerun" or "Update" button
- New version deploys in 1-2 minutes

---

## Monitoring & Maintenance

### Weekly Checks

1. **Test Application**
   - Generate a sample summary
   - Verify all input methods work
   - Check history functionality

2. **Monitor Performance**
   - Note response times
   - Check for errors in app

### Monthly Updates

1. **Update Dependencies** (Optional)
   - Check for package updates
   - Test locally before updating
   - Commit and push changes

```bash
# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade package-name

# Update requirements.txt
pip freeze > requirements.txt
```

2. **Review Statistics**
   - Check app traffic (if enabled)
   - Monitor usage patterns

### Occasional Maintenance

1. **Clear Cache** (if needed)
   - Streamlit Cloud automatically manages cache
   - No manual action usually required

2. **App Restart**
   - Automatic daily restart
   - Manual restart: Settings → "Always rerun"

---

## Performance Optimization

### Model Selection for Deployment

```
For Streamlit Cloud (Optimal):
- distilbart-cnn-6-6 (Fast, lightweight)
- facebook/bart-large-cnn (Default, balanced)

For Premium Tier or Local:
- google/pegasus-cnn_dailymail (Detailed)
- t5-base (Versatile)
```

### Text Processing Tips

1. **Batch Processing**
   - Process multiple texts in sessions
   - Leverage model caching

2. **Optimize Input Size**
   - Truncate very long texts
   - Streamline preprocessing

3. **Cache Configuration**
   ```python
   @st.cache_resource
   def load_summarization_pipeline(model_name):
       # Automatically cached by Streamlit
       return pipeline("summarization", model=model_name)
   ```

---

## Useful Links

- **Streamlit Cloud Docs:** https://docs.streamlit.io/streamlit-cloud
- **GitHub Help:** https://docs.github.com
- **Streamlit Community:** https://discuss.streamlit.io
- **HuggingFace Models:** https://huggingface.co/models?task=summarization

---

## Quick Reference

| Action | Command |
|--------|---------|
| Test locally | `streamlit run streamlit_app.py` |
| Push to GitHub | `git push origin main` |
| Trigger redeploy | Push changes to main branch |
| View logs | Click "⋮" → "View logs" in Streamlit Cloud |
| Add secrets | Settings → Secrets in Streamlit Cloud |

---

## Support

If you encounter issues:

1. **Check Streamlit Cloud Logs**
   - Click "⋮" menu → "View logs"
   - Look for error messages

2. **Test Locally First**
   - Ensure app works locally with `streamlit run streamlit_app.py`

3. **Check Requirements**
   - Verify all packages listed in `requirements.txt`

4. **Community Help**
   - Post in Streamlit Discord: https://discord.gg/streamlit
   - Ask on GitHub Discussions

---

**Deployment Complete! 🎉**

Your app is now live and accessible to anyone with the URL.
