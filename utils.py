"""
Utility functions for the Content Summarizer application.
Handles text extraction, URL processing, and NLP model interactions.
"""

import re
from typing import Optional, Tuple
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import PyPDF2
from transformers import pipeline, AutoTokenizer
import streamlit as st

# ============================================================================
# CONSTANTS
# ============================================================================

AVAILABLE_MODELS = {
    "facebook/bart-large-cnn": "BART (Fast & Accurate)",
    "google/pegasus-cnn_dailymail": "PEGASUS (Detailed)",
    "t5-base": "T5 (General Purpose)",
    "distilbart-cnn-6-6": "DistilBART (Lightweight)",
}

SUMMARY_LENGTHS = {
    "Short": 0.2,      # 20% of original
    "Medium": 0.3,     # 30% of original
    "Long": 0.5,       # 50% of original
}

# ============================================================================
# TEXT EXTRACTION FUNCTIONS
# ============================================================================

def extract_text_from_pdf(pdf_file) -> str:
    """
    Extract text from an uploaded PDF file.
    
    Args:
        pdf_file: Streamlit UploadedFile object
        
    Returns:
        Extracted text as string
    """
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF")
        
        return text.strip()
    
    except Exception as e:
        raise Exception(f"Error extracting PDF: {str(e)}")

def validate_url(url: str) -> bool:
    """
    Validate if a URL is properly formatted.
    
    Args:
        url: URL string to validate
        
    Returns:
        Boolean indicating if URL is valid
    """
    try:
        result = urlparse(url)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except Exception:
        return False

def extract_text_from_url(url: str) -> str:
    """
    Extract readable text content from a URL.
    
    Args:
        url: URL to fetch and extract text from
        
    Returns:
        Extracted text as string
        
    Raises:
        Exception: If URL fetching or parsing fails
    """
    try:
        # Set timeout and user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(['script', 'style', 'nav', 'footer']):
            script.decompose()
        
        # Extract text
        text = soup.get_text(separator='\n')
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        text = '\n'.join(line for line in lines if line)
        
        if not text.strip():
            raise ValueError("No text content found in the webpage")
        
        return text.strip()
    
    except requests.RequestException as e:
        raise Exception(f"Error fetching URL: {str(e)}")
    except Exception as e:
        raise Exception(f"Error processing URL content: {str(e)}")

# ============================================================================
# TEXT PREPROCESSING
# ============================================================================

def clean_text(text: str) -> str:
    """
    Clean and normalize text for better summarization.
    
    Args:
        text: Raw text to clean
        
    Returns:
        Cleaned text
    """
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters but keep sentence structure
    text = re.sub(r'[^\w\s.!?,-]', '', text)
    
    return text.strip()

def truncate_text(text: str, max_length: int = 1024) -> str:
    """
    Truncate text to a maximum length while preserving sentence structure.
    
    Args:
        text: Text to truncate
        max_length: Maximum length in characters
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    # Try to break at sentence boundary
    truncated = text[:max_length]
    last_period = truncated.rfind('.')
    
    if last_period > max_length * 0.7:  # If period is reasonably close
        return truncated[:last_period + 1]
    
    return truncated + "..."

# ============================================================================
# SUMMARIZATION FUNCTIONS
# ============================================================================

@st.cache_resource
def load_summarization_pipeline(model_name: str):
    """
    Load a summarization pipeline with caching.
    
    Args:
        model_name: Model identifier from HuggingFace
        
    Returns:
        Loaded pipeline object
    """
    try:
        return pipeline("summarization", model=model_name)
    except Exception as e:
        raise Exception(f"Error loading model {model_name}: {str(e)}")

def get_target_length(text: str, length_ratio: float) -> Tuple[int, int]:
    """
    Calculate target summary length based on input and ratio.
    
    Args:
        text: Input text
        length_ratio: Desired ratio of summary to original (0.0-1.0)
        
    Returns:
        Tuple of (min_length, max_length)
    """
    # Get word count
    words = len(text.split())
    
    # Calculate target based on ratio
    target_words = max(10, int(words * length_ratio))
    
    # Models typically work better with these constraints
    min_length = max(10, int(target_words * 0.7))
    max_length = max(15, int(target_words * 1.3))
    
    return min_length, max_length

def generate_summary(
    text: str,
    model_name: str = "facebook/bart-large-cnn",
    summary_length: str = "Medium"
) -> str:
    """
    Generate a summary of the input text using a transformer model.
    
    Args:
        text: Input text to summarize
        model_name: Model to use for summarization
        summary_length: Length category ('Short', 'Medium', 'Long')
        
    Returns:
        Generated summary text
        
    Raises:
        Exception: If summarization fails
    """
    try:
        # Validate input
        text = clean_text(text)
        
        if not text or len(text) < 50:
            raise ValueError("Text must be at least 50 characters long")
        
        # Get the length ratio
        length_ratio = SUMMARY_LENGTHS.get(summary_length, 0.3)
        
        # Load model
        summarizer = load_summarization_pipeline(model_name)
        
        # Calculate target lengths
        min_length, max_length = get_target_length(text, length_ratio)
        
        # Truncate if text is too long (most models have ~1024 token limit)
        truncated_text = truncate_text(text, max_length=1024)
        
        # Generate summary
        summary = summarizer(
            truncated_text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        
        summary_text = summary[0]['summary_text']
        
        return summary_text.strip()
    
    except Exception as e:
        raise Exception(f"Summarization failed: {str(e)}")

def generate_abstractive_summary_advanced(
    text: str,
    num_sentences: int = 3,
    model_name: str = "facebook/bart-large-cnn"
) -> str:
    """
    Generate a more advanced abstractive summary with specific sentence count.
    
    Args:
        text: Input text
        num_sentences: Target number of sentences in summary
        model_name: Model to use
        
    Returns:
        Generated summary
    """
    try:
        text = clean_text(text)
        
        # Estimate words per sentence
        sentences = text.split('.')
        if len(sentences) <= 1:
            sentences = text.split('\n')
        
        valid_sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        if not valid_sentences:
            raise ValueError("Could not parse text into sentences")
        
        # Estimate target length
        avg_words_per_sentence = len(text.split()) / len(valid_sentences)
        target_words = num_sentences * avg_words_per_sentence
        
        # Load and generate
        summarizer = load_summarization_pipeline(model_name)
        
        min_length = max(10, int(target_words * 0.6))
        max_length = int(target_words * 1.4)
        
        summary = summarizer(
            truncate_text(text, max_length=1024),
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        
        return summary[0]['summary_text'].strip()
    
    except Exception as e:
        raise Exception(f"Advanced summarization failed: {str(e)}")

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def calculate_compression_ratio(original: str, summary: str) -> float:
    """
    Calculate the compression ratio of a summary.
    
    Args:
        original: Original text
        summary: Summary text
        
    Returns:
        Compression ratio as percentage
    """
    if not original:
        return 0.0
    
    return (1 - len(summary) / len(original)) * 100

def estimate_reading_time(text: str, words_per_minute: int = 200) -> float:
    """
    Estimate reading time in minutes.
    
    Args:
        text: Text to estimate
        words_per_minute: Reading speed
        
    Returns:
        Estimated reading time in minutes
    """
    word_count = len(text.split())
    return word_count / words_per_minute

def extract_key_info(text: str) -> dict:
    """
    Extract basic information about the text.
    
    Args:
        text: Input text
        
    Returns:
        Dictionary with text statistics
    """
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    
    return {
        "character_count": len(text),
        "word_count": len(text.split()),
        "sentence_count": len(sentences),
        "avg_sentence_length": len(text.split()) / len(sentences) if sentences else 0,
        "reading_time_minutes": estimate_reading_time(text)
    }
