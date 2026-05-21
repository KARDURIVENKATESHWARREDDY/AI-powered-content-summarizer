# 📝 AI-Powered Content Summarizer

A full-stack web application built with **Python**, **Streamlit**, and **Hugging Face Transformers** for generating intelligent summaries from text, PDFs, and URLs using state-of-the-art NLP models.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://summarizer.streamlit.app)

---

## ✨ Features

### Core Functionality
- **Multi-source Input Support**
  - 📝 Direct text input
  - 📄 PDF file upload with automatic text extraction
  - 🌐 URL fetching and content extraction

- **Advanced Summarization**
  - Multiple state-of-the-art NLP models (BART, PEGASUS, T5, DistilBART)
  - Adjustable summary lengths (Short, Medium, Long)
  - Automatic text preprocessing and normalization
  - Intelligent sentence boundary detection

- **Modern User Interface**
  - Beautiful gradient design with custom CSS
  - Real-time statistics and metrics
  - Responsive layout for desktop and mobile
  - Intuitive input controls

- **Summary Management**
  - 📚 Persistent history with JSON storage
  - 🔄 Quick history loading
  - 📋 Copy to clipboard functionality
  - 📥 Download summaries as .txt files
  - 📊 Export statistics as CSV

- **Advanced Metrics**
  - Compression ratio calculation
  - Character and word counts
  - Reading time estimation
  - Model and parameters display

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda
- Git (for cloning)

### Local Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/AI-powered-content-summarizer.git
cd AI-powered-content-summarizer
```

2. **Create Virtual Environment**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n summarizer python=3.10
conda activate summarizer
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
streamlit run streamlit_app.py
```

The application will open at `http://localhost:8501`

---

## 📦 Project Structure

```
AI-powered-content-summarizer/
├── streamlit_app.py          # Main Streamlit application
├── utils.py                   # Utility functions for text processing
├── requirements.txt           # Python dependencies
├── .streamlit/
│   └── config.toml           # Streamlit configuration
├── .gitignore                # Git ignore rules
├── README.md                 # This file
└── LICENSE                   # MIT License
```

### File Descriptions

| File | Description |
|------|-------------|
| `streamlit_app.py` | Main application with UI components, session management, and history handling |
| `utils.py` | Utility functions for PDF/URL extraction, text cleaning, and summarization |
| `requirements.txt` | All Python package dependencies with specific versions |
| `.streamlit/config.toml` | Streamlit theming and server configuration |

---

## 🎨 Available Models

### 1. **facebook/bart-large-cnn** (Default - Recommended)
- **Speed:** ⚡⚡⚡ Fast
- **Quality:** ⭐⭐⭐⭐⭐ Excellent
- **Use Case:** News articles, blogs, general text
- **Size:** 1.6GB
- **Details:** Optimized for CNN/DailyMail dataset, produces coherent abstractive summaries

### 2. **google/pegasus-cnn_dailymail**
- **Speed:** ⚡⚡ Moderate
- **Quality:** ⭐⭐⭐⭐⭐ Excellent
- **Use Case:** Detailed articles, news stories
- **Size:** 2.1GB
- **Details:** Designed specifically for news summarization, very detail-oriented

### 3. **t5-base**
- **Speed:** ⚡⚡ Moderate
- **Quality:** ⭐⭐⭐⭐ Very Good
- **Use Case:** General purpose, diverse text types
- **Size:** 892MB
- **Details:** Versatile transformer, works well across different domains

### 4. **distilbart-cnn-6-6**
- **Speed:** ⚡⚡⚡ Very Fast
- **Quality:** ⭐⭐⭐⭐ Good
- **Use Case:** Quick summaries, resource-constrained environments
- **Size:** 306MB
- **Details:** Lightweight version of BART, best for CPU-only systems

---

## 🎯 Summary Length Options

| Length | Ratio | Best For |
|--------|-------|----------|
| **Short** | 20% | Quick overviews, key points |
| **Medium** | 30% | Balanced summaries (recommended) |
| **Long** | 50% | Comprehensive summaries, detail retention |

---

## 🌐 Deployment on Streamlit Cloud

### Step 1: Prepare GitHub Repository

1. **Create a GitHub Account** (if you don't have one)
   - Visit https://github.com and sign up

2. **Create a New Repository**
   - Name it: `AI-powered-content-summarizer`
   - Add `.gitignore` (select Python)
   - Initialize with README

3. **Push Local Code to GitHub**
```bash
# Initialize git locally (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Content Summarizer"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/AI-powered-content-summarizer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit https://share.streamlit.io
   - Click "Sign up with GitHub" or "Sign in"

2. **Deploy Your App**
   - Click "New app" button
   - Select your GitHub repository
   - Choose the branch (main)
   - Set the main file path to `streamlit_app.py`
   - Click "Deploy"

3. **Wait for Deployment**
   - First deployment takes 2-5 minutes
   - You'll get a unique URL like `https://yourusername-summarizer.streamlit.app`

### Step 3: Configure Streamlit Cloud Settings (Optional)

1. **Access App Settings**
   - Click the menu (⋮) in the top right
   - Select "Settings"

2. **Advanced Settings** (if needed)
   - Python version: 3.10+
   - Install dependencies from: `requirements.txt`

### Step 4: Share Your App

- Copy the URL from the browser
- Share with others
- The app is now live and accessible 24/7

---

## 🔧 Configuration & Customization

### Customizing the Theme

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#667eea"        # Change primary color
backgroundColor = "#f0f2f6"     # Background color
secondaryBackgroundColor = "#e8eef9"  # Secondary background
textColor = "#262730"           # Text color
font = "sans serif"             # Font family
```

### Adjusting Model Settings

Edit `utils.py` to change default models:

```python
AVAILABLE_MODELS = {
    "facebook/bart-large-cnn": "BART (Fast & Accurate)",
    # Add or remove models here
}

SUMMARY_LENGTHS = {
    "Short": 0.2,
    "Medium": 0.3,
    "Long": 0.5,
}
```

### Changing Upload/History Limits

In `streamlit_app.py`:

```python
# Change history limit (line ~130)
if len(st.session_state.history) > 50:  # Modify 50
    st.session_state.history = st.session_state.history[:50]

# Change max file size in config.toml
maxUploadSize = 200  # MB
```

---

## 📊 Usage Examples

### Example 1: Summarize a News Article
1. Select "URL" input method
2. Paste a news article URL (e.g., from BBC, CNN)
3. Choose "Medium" length
4. Select "facebook/bart-large-cnn" model
5. Click "Generate Summary"
6. Download or copy the result

### Example 2: Process Research Paper
1. Select "PDF" input method
2. Upload your PDF
3. Choose "Long" length for comprehensive summary
4. Use "google/pegasus-cnn_dailymail" for detailed output
5. Export statistics as CSV

### Example 3: Quick Text Summarization
1. Select "Text" input method
2. Paste or type content (minimum 50 characters)
3. Choose "Short" length for quick overview
4. Use "distilbart-cnn-6-6" for faster processing
5. Copy to clipboard or download

---

## 🛠️ Troubleshooting

### Issue: Model Download is Slow
**Solution:** First model download might take 5-15 minutes depending on internet speed. Subsequent runs are cached.

### Issue: Out of Memory Error
**Solution:** 
- Use lighter models: `distilbart-cnn-6-6`
- Reduce text length or use shorter summaries
- On Streamlit Cloud, models are cached after first load

### Issue: PDF Extraction Fails
**Solution:**
- Ensure PDF is readable (not image-based)
- Check file size (under 200MB)
- Try uploading a different PDF format

### Issue: URL Extraction Returns Empty
**Solution:**
- Verify URL is valid and accessible
- Try a different URL (some sites block scrapers)
- Check your internet connection

### Issue: History Not Saving
**Solution:**
- Check write permissions in `~/.summarizer_history.json`
- Ensure sufficient disk space
- File path should be writable

---

## 📈 Performance Tips

### Optimization for Streamlit Cloud

1. **Use Lightweight Models**
   - `distilbart-cnn-6-6` for consistent performance

2. **Enable Caching**
   - Models are cached automatically with `@st.cache_resource`

3. **Optimize Text Length**
   - Keep input texts under 1000 words for faster processing

4. **Monitor Resources**
   - Use `Short` summaries for real-time processing

### Local Machine Tips

1. **GPU Acceleration**
   - Install `torch` with CUDA support for faster processing
   - Download specific model on first run

2. **Memory Management**
   - Monitor RAM usage with large PDFs
   - Process text in batches if needed

---

## 🔐 Security Considerations

- **Input Validation:** All URLs and uploads are validated
- **Resource Limits:** Max file size 200MB, text limited to 1024 tokens for models
- **Data Privacy:** History stored locally in `~/.summarizer_history.json`
- **No External Logging:** Your content isn't logged to external services

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Additional language support
- More NLP models
- Enhanced UI/UX
- Performance optimizations
- Bug fixes and testing

---

## 💡 Future Enhancements

- [ ] Multi-language summarization support
- [ ] Custom model fine-tuning interface
- [ ] Batch processing for multiple files
- [ ] API endpoint for programmatic access
- [ ] Advanced analytics dashboard
- [ ] User authentication and accounts
- [ ] Comparison between different models
- [ ] Video transcript summarization

---

## 📞 Support & Contact

If you encounter any issues or have suggestions:

1. **GitHub Issues:** Open an issue on the repository
2. **Email:** Send to [your-email@example.com]
3. **Streamlit Community:** Post in the Streamlit forum

---

## 🙏 Acknowledgments

- **Hugging Face** for the Transformers library and pre-trained models
- **Streamlit** for the amazing web framework
- **PyPDF2** for PDF processing
- **BeautifulSoup** for web scraping
- All contributors and users for feedback and improvements

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- [NLP Models Hub](https://huggingface.co/models?task=summarization)

---

**Made with ❤️ using Python, Streamlit, and Transformers**

Last Updated: 2026-05-21
#   A I - p o w e r e d - c o n t e n t - s u m m a r i z e r  
 