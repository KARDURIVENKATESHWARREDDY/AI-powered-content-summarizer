# 📚 Developer Guide

This guide is for developers who want to contribute, extend, or maintain the AI Content Summarizer project.

---

## Table of Contents

1. [Project Architecture](#project-architecture)
2. [Development Setup](#development-setup)
3. [Code Structure](#code-structure)
4. [Adding Features](#adding-features)
5. [Testing](#testing)
6. [Contributing](#contributing)
7. [Performance Optimization](#performance-optimization)

---

## Project Architecture

### Overview

```
┌─────────────────────────────────────────────┐
│       Streamlit UI (streamlit_app.py)       │
├─────────────────────────────────────────────┤
│    Session Management & Caching Layer       │
├─────────────────────────────────────────────┤
│   Utility Functions (utils.py)              │
│  ┌─────────────────────────────────────┐    │
│  │ • Text extraction                   │    │
│  │ • URL processing                    │    │
│  │ • PDF handling                      │    │
│  │ • Text cleaning                     │    │
│  │ • NLP model management              │    │
│  └─────────────────────────────────────┘    │
├─────────────────────────────────────────────┤
│    External Services                        │
│  ┌─────────────────────────────────────┐    │
│  │ • Hugging Face Transformers         │    │
│  │ • BeautifulSoup (Web scraping)      │    │
│  │ • PyPDF2 (PDF processing)           │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

### Component Interactions

```
User Input
    ↓
streamlit_app.py → Input Validation
    ↓
utils.py → Content Extraction
    ↓
utils.py → Text Preprocessing
    ↓
utils.py → NLP Model Processing
    ↓
streamlit_app.py → Display Results
    ↓
streamlit_app.py → History Storage
    ↓
JSON File (.summarizer_history.json)
```

---

## Development Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-powered-content-summarizer.git
cd AI-powered-content-summarizer
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Development Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. Verify Installation

```bash
# Test import
python -c "import streamlit; import transformers; print('✅ All dependencies installed')"

# Run app
streamlit run streamlit_app.py
```

---

## Code Structure

### `streamlit_app.py` (Main Application)

**Sections:**
- Page Configuration (UI setup)
- Custom CSS (Styling)
- Session State (Data management)
- History Management (Persistence)
- Main Function (UI logic)

**Key Classes/Functions:**
```python
load_history()              # Load summary history from file
save_history(history)       # Save history to file
add_to_history()           # Add new summary to history
clear_history()            # Clear all history
main()                     # Main application logic
```

**Flow:**
1. Initialize session state
2. Load history from file
3. Setup sidebar configuration
4. Render input section
5. Process user input
6. Generate summary
7. Display results
8. Save to history

### `utils.py` (Utility Functions)

**Main Modules:**

#### Text Extraction
```python
extract_text_from_pdf(pdf_file)      # PDF → text
extract_text_from_url(url)           # URL → text
validate_url(url)                    # URL validation
clean_text(text)                     # Text cleaning
truncate_text(text, max_length)      # Text truncation
```

#### NLP Processing
```python
load_summarization_pipeline(model)   # Load model (cached)
generate_summary()                   # Generate summary
generate_abstractive_summary_advanced()  # Advanced summarization
```

#### Helpers
```python
get_target_length()                  # Calculate summary length
calculate_compression_ratio()        # Compression metrics
estimate_reading_time()              # Reading time estimation
extract_key_info()                   # Extract text statistics
```

---

## Adding Features

### Example 1: Add New Summarization Model

1. **Update `utils.py`:**

```python
AVAILABLE_MODELS = {
    "facebook/bart-large-cnn": "BART (Fast & Accurate)",
    "google/pegasus-cnn_dailymail": "PEGASUS (Detailed)",
    "t5-base": "T5 (General Purpose)",
    "distilbart-cnn-6-6": "DistilBART (Lightweight)",
    "new-model-name": "New Model (Description)",  # Add new model
}
```

2. **Test Model:**

```python
# Test script
from utils import generate_summary

text = "Your test text..."
summary = generate_summary(text, model_name="new-model-name")
print(summary)
```

3. **Update README.md** with model information

### Example 2: Add Download Format

**Current:** Text file

**To Add:** PDF, Markdown, etc.

1. **Install dependency:**
```bash
pip install reportlab  # For PDF
```

2. **Add function to `utils.py`:**

```python
def export_to_pdf(summary, original_text, metadata):
    """Export summary to PDF format"""
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    
    # PDF generation logic
    pass
```

3. **Update `streamlit_app.py`:**

```python
if st.button("📄 Download as PDF"):
    pdf_data = export_to_pdf(
        summary,
        original_text,
        metadata
    )
    st.download_button(
        label="📥 Download PDF",
        data=pdf_data,
        file_name=f"summary_{timestamp}.pdf",
        mime="application/pdf"
    )
```

### Example 3: Add Multi-language Support

1. **Create translation mapping:**

```python
# translations.py
TRANSLATIONS = {
    "en": {
        "title": "AI Content Summarizer",
        "input_text": "Paste or type your content here:",
        # ... more translations
    },
    "es": {
        "title": "Resumidor de Contenido IA",
        "input_text": "Pegue o escriba su contenido aquí:",
        # ... more translations
    }
}
```

2. **Update `streamlit_app.py`:**

```python
language = st.selectbox("Language", ["English", "Español", "Français"])

# Use translations
st.write(TRANSLATIONS[lang_map[language]]["input_text"])
```

---

## Testing

### Unit Tests

**Create `test_utils.py`:**

```python
import pytest
from utils import clean_text, validate_url, calculate_compression_ratio

def test_clean_text():
    """Test text cleaning"""
    text = "  Hello   world  "
    assert clean_text(text) == "Hello world"

def test_validate_url():
    """Test URL validation"""
    assert validate_url("https://example.com") == True
    assert validate_url("invalid-url") == False

def test_compression_ratio():
    """Test compression calculation"""
    original = "This is a long text that will be summarized"
    summary = "This text summarized"
    ratio = calculate_compression_ratio(original, summary)
    assert 0 <= ratio <= 100
```

**Run tests:**

```bash
pytest test_utils.py -v
```

### Integration Tests

**Create `test_integration.py`:**

```python
import streamlit as st
from streamlit.testing.v1 import AppTest

def test_app_loads():
    """Test app loads without errors"""
    at = AppTest.from_file("streamlit_app.py")
    at.run()
    assert not at.exception

def test_summary_generation():
    """Test summary generation end-to-end"""
    # Test text summarization flow
    pass
```

### Manual Testing Checklist

- [ ] Text summarization works
- [ ] PDF upload processes correctly
- [ ] URL extraction functions
- [ ] All models load without errors
- [ ] History saves and loads
- [ ] Download works
- [ ] UI is responsive
- [ ] Error handling works

---

## Performance Optimization

### 1. Model Caching

**Already implemented:**
```python
@st.cache_resource
def load_summarization_pipeline(model_name: str):
    return pipeline("summarization", model=model_name)
```

**Benefits:**
- Models load only once
- Subsequent requests instant
- Shared across user sessions

### 2. Text Truncation

**Already implemented:**
```python
def truncate_text(text: str, max_length: int = 1024) -> str:
    # Truncate at sentence boundary
    # Prevents out-of-memory errors
    pass
```

### 3. Lazy Loading

**To implement:**
```python
# Load models on-demand instead of startup
@st.cache_resource
def get_available_models():
    # Return only model names, not loaded models
    return list(AVAILABLE_MODELS.keys())
```

### 4. Batch Processing

**To implement:**
```python
def process_batch(texts, model_name):
    """Process multiple texts efficiently"""
    summarizer = load_summarization_pipeline(model_name)
    summaries = []
    for text in texts:
        summary = summarizer(text, ...)
        summaries.append(summary)
    return summaries
```

### 5. Memory Management

```python
# Monitor memory usage
import psutil

def check_memory():
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # MB

# Log memory usage
memory_mb = check_memory()
st.caption(f"Memory: {memory_mb:.1f} MB")
```

---

## Code Style

### PEP 8 Compliance

**Use Black formatter:**
```bash
black streamlit_app.py utils.py
```

**Use Flake8 linter:**
```bash
flake8 streamlit_app.py utils.py
```

**Use isort for imports:**
```bash
isort streamlit_app.py utils.py
```

### Naming Conventions

```python
# Functions: snake_case
def extract_text_from_pdf():
    pass

# Classes: PascalCase
class ContentProcessor:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_FILE_SIZE = 200

# Private methods: _snake_case
def _internal_helper():
    pass
```

### Documentation

**Function docstrings:**
```python
def generate_summary(text: str, model_name: str) -> str:
    """
    Generate a summary of the input text.
    
    Args:
        text: Input text to summarize
        model_name: Name of the model to use
        
    Returns:
        Generated summary text
        
    Raises:
        ValueError: If text is too short
        Exception: If model loading fails
        
    Examples:
        >>> text = "Long text here..."
        >>> summary = generate_summary(text, "facebook/bart-large-cnn")
    """
    pass
```

---

## Contributing

### Workflow

1. **Fork repository**
2. **Create feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make changes and commit**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   ```
4. **Push to GitHub**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Create Pull Request**
   - Describe changes
   - Reference issues
   - Add tests

### Before Submitting PR

- [ ] Code passes `black` formatting
- [ ] Code passes `flake8` linting
- [ ] Tests pass with `pytest`
- [ ] README updated if needed
- [ ] No hardcoded values
- [ ] Type hints added
- [ ] Docstrings included

---

## Debugging

### Enable Debug Logging

```bash
streamlit run streamlit_app.py --logger.level=debug
```

### Add Debug Statements

```python
st.write("Debug:", variable)  # Display in UI
print("Debug:", variable)     # Console output
```

### Profiling

```bash
# Install profiler
pip install py-spy

# Run with profiler
py-spy record -o profile.svg -- streamlit run streamlit_app.py
```

---

## Useful Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **Transformers Docs:** https://huggingface.co/docs/transformers
- **Python Docs:** https://docs.python.org/3
- **Git Documentation:** https://git-scm.com/doc

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Model takes too long | Use lighter model like DistilBART |
| Memory errors | Reduce text length or use smaller model |
| Import errors | Run `pip install -r requirements-dev.txt` |
| UI not updating | Clear Streamlit cache: `streamlit cache clear` |

---

**Happy coding! 🚀**

Questions? Open an issue on GitHub or reach out to the community.
