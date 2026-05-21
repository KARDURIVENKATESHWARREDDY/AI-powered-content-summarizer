"""
AI-Powered Content Summarizer
A full-stack web application for generating concise summaries from text, PDFs, and URLs.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os
from pathlib import Path
import pyperclip
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()
HF_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

from utils import (
    extract_text_from_pdf,
    extract_text_from_url,
    generate_summary,
    AVAILABLE_MODELS,
    SUMMARY_LENGTHS,
    validate_url
)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="AI Content Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "An AI-powered tool to summarize content from text, PDFs, and URLs.",
    }
)

# ============================================================================
# CUSTOM CSS
# ============================================================================

st.markdown("""
    <style>
    /* Main styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .header-container h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .header-container p {
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
        opacity: 0.95;
    }
    
    /* Card styling */
    .summary-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .summary-card h3 {
        margin-top: 0;
        color: #667eea;
    }
    
    /* Input area styling */
    .input-container {
        background: #f0f2f6;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Stats styling */
    .stats-container {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        flex: 1;
        min-width: 150px;
        text-align: center;
    }
    
    .stat-box h4 {
        margin: 0;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .stat-box .value {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 0.5rem;
    }
    
    /* History styling */
    .history-item {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 6px;
        margin: 0.5rem 0;
    }
    
    .history-item:hover {
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Button styling */
    .download-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        border: none;
        cursor: pointer;
    }
    
    /* Alert styling */
    .alert-info {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .alert-success {
        background: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .alert-warning {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "current_summary" not in st.session_state:
    st.session_state.current_summary = None

if "current_original_text" not in st.session_state:
    st.session_state.current_original_text = None

# ============================================================================
# HISTORY MANAGEMENT
# ============================================================================

HISTORY_FILE = Path(os.path.expanduser("~/.summarizer_history.json"))

def load_history():
    """Load history from file."""
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            st.warning(f"Could not load history: {e}")
            return []
    return []

def save_history(history):
    """Save history to file."""
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.warning(f"Could not save history: {e}")

def add_to_history(content_type, original_text, summary, model, length):
    """Add a summary to the history."""
    st.session_state.history.insert(0, {
        "timestamp": datetime.now().isoformat(),
        "type": content_type,
        "original_text": original_text[:100] + "..." if len(original_text) > 100 else original_text,
        "summary": summary,
        "model": model,
        "length": length,
        "original_length": len(original_text),
        "summary_length": len(summary)
    })
    
    # Keep only last 50 items
    if len(st.session_state.history) > 50:
        st.session_state.history = st.session_state.history[:50]
    
    save_history(st.session_state.history)

def clear_history():
    """Clear all history."""
    st.session_state.history = []
    save_history([])
    st.success("History cleared!")

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    # Header
    st.markdown("""
        <div class="header-container">
            <h1>📝 AI Content Summarizer</h1>
            <p>Transform long content into concise summaries using advanced NLP models</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Model Selection
        selected_model = st.selectbox(
            "Select Summarization Model",
            options=list(AVAILABLE_MODELS.keys()),
            help="Different models offer different quality and speed trade-offs"
        )

        if HF_API_TOKEN:
            st.success("🔐 Hugging Face API token loaded from .env")
        else:
            st.info("Add HUGGINGFACEHUB_API_TOKEN to .env to use private Hugging Face models")
        
        # Summary Length
        summary_length = st.select_slider(
            "Summary Length",
            options=list(SUMMARY_LENGTHS.keys()),
            value="Medium",
            help="Choose how concise your summary should be"
        )
        
        st.divider()
        
        # History Section
        st.subheader("📚 Summary History")
        
        if st.button("🔄 Refresh History"):
            st.session_state.history = load_history()
            st.rerun()
        
        if st.button("🗑️ Clear History", type="secondary"):
            clear_history()
            st.rerun()
        
        history_count = len(st.session_state.history)
        st.metric("Total Summaries", history_count)
        
        if history_count > 0:
            with st.expander("View History", expanded=False):
                for idx, item in enumerate(st.session_state.history[:10]):
                    timestamp = datetime.fromisoformat(item["timestamp"]).strftime("%Y-%m-%d %H:%M")
                    st.markdown(f"""
                        **{idx + 1}. {item['type'].upper()}** | {timestamp}  
                        Model: {item['model']} | Length: {item['length']}
                        """)
                    
                    if st.button(
                        "Load",
                        key=f"load_{idx}",
                        help=f"Load this summary"
                    ):
                        st.session_state.current_summary = item["summary"]
                        st.session_state.current_original_text = item["original_text"]
                        st.rerun()
    
    # Main Content Area
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.markdown("#### 📊 Statistics")
        if st.session_state.history:
            avg_compression = sum(
                (item['original_length'] - item['summary_length']) / item['original_length'] * 100
                for item in st.session_state.history
            ) / len(st.session_state.history)
            st.metric("Avg Compression", f"{avg_compression:.1f}%")
            st.metric("Total Summaries", len(st.session_state.history))
    
    with col1:
        st.markdown("#### 📥 Input Method")
        input_method = st.segmented_control(
            "Choose input method:",
            ["Text", "PDF", "URL"],
            selection_mode="single",
        )
    
    st.divider()
    
    # Input Section Based on Selection
    input_text = ""
    source_type = ""
    
    if input_method == "Text":
        st.markdown("#### ✏️ Enter Text")
        input_text = st.text_area(
            "Paste or type your content here:",
            height=200,
            placeholder="Enter the text you want to summarize...",
            label_visibility="collapsed"
        )
        source_type = "Text"
    
    elif input_method == "PDF":
        st.markdown("#### 📄 Upload PDF")
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type=["pdf"],
            label_visibility="collapsed"
        )
        
        if uploaded_file is not None:
            st.info(f"📁 File uploaded: {uploaded_file.name}")
            try:
                input_text = extract_text_from_pdf(uploaded_file)
                source_type = "PDF"
                if input_text:
                    st.success(f"✅ Extracted {len(input_text)} characters from PDF")
            except Exception as e:
                st.error(f"❌ Error processing PDF: {str(e)}")
    
    elif input_method == "URL":
        st.markdown("#### 🌐 Enter URL")
        url_input = st.text_input(
            "Enter a URL",
            placeholder="https://example.com/article",
            label_visibility="collapsed"
        )
        
        if url_input:
            if validate_url(url_input):
                st.info(f"🔗 Processing: {url_input}")
                try:
                    input_text = extract_text_from_url(url_input)
                    source_type = "URL"
                    if input_text:
                        st.success(f"✅ Extracted {len(input_text)} characters from URL")
                except Exception as e:
                    st.error(f"❌ Error fetching URL: {str(e)}")
            else:
                st.error("❌ Please enter a valid URL (starting with http:// or https://)")
    
    st.divider()
    
    # Summarization Section
    if st.button("🚀 Generate Summary", type="primary", use_container_width=True):
        if not input_text or input_text.strip() == "":
            st.error("⚠️ Please provide content to summarize!")
        elif len(input_text.strip()) < 50:
            st.error("⚠️ Content is too short. Please provide at least 50 characters.")
        else:
            with st.spinner(f"🔄 Generating {summary_length.lower()} summary using {selected_model}..."):
                try:
                    summary = generate_summary(
                        input_text,
                        model_name=selected_model,
                        summary_length=summary_length
                    )
                    
                    st.session_state.current_summary = summary
                    st.session_state.current_original_text = input_text
                    
                    # Add to history
                    add_to_history(
                        source_type,
                        input_text,
                        summary,
                        selected_model,
                        summary_length
                    )
                    
                    st.success("✅ Summary generated successfully!")
                    
                except Exception as e:
                    st.error(f"❌ Error generating summary: {str(e)}")
    
    # Display Current Summary
    if st.session_state.current_summary:
        st.markdown("---")
        st.markdown("#### 📋 Summary Result")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Original Length", f"{len(st.session_state.current_original_text)} chars")
        with col2:
            st.metric("Summary Length", f"{len(st.session_state.current_summary)} chars")
        with col3:
            compression = (1 - len(st.session_state.current_summary) / len(st.session_state.current_original_text)) * 100
            st.metric("Compression", f"{compression:.1f}%")
        
        # Summary Display
        st.markdown("""
            <div class="summary-card">
        """, unsafe_allow_html=True)
        
        st.markdown(st.session_state.current_summary)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Action Buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                try:
                    pyperclip.copy(st.session_state.current_summary)
                    st.success("✅ Copied to clipboard!")
                except:
                    st.info("📋 Copy the text manually from the summary above")
        
        with col2:
            summary_text = f"""AI CONTENT SUMMARIZER - SUMMARY REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ORIGINAL TEXT ({len(st.session_state.current_original_text)} characters):
{st.session_state.current_original_text[:500]}...

SUMMARY ({len(st.session_state.current_summary)} characters):
{st.session_state.current_summary}

---
Generated using AI Content Summarizer
Model: {selected_model}
Length: {summary_length}
Compression Ratio: {(1 - len(st.session_state.current_summary) / len(st.session_state.current_original_text)) * 100:.1f}%
"""
            st.download_button(
                label="📥 Download Summary",
                data=summary_text,
                file_name=f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col3:
            csv_data = pd.DataFrame({
                "Metric": ["Original Length", "Summary Length", "Compression Ratio", "Model Used", "Summary Length Type"],
                "Value": [
                    len(st.session_state.current_original_text),
                    len(st.session_state.current_summary),
                    f"{(1 - len(st.session_state.current_summary) / len(st.session_state.current_original_text)) * 100:.1f}%",
                    selected_model,
                    summary_length
                ]
            })
            st.download_button(
                label="📊 Export Stats",
                data=csv_data.to_csv(index=False),
                file_name=f"summary_stats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )

if __name__ == "__main__":
    main()
