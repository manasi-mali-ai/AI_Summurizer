import streamlit as st
from utils.loader import load_pdf
from utils.summarizer import summarize_chunks
from utils.youtube_transcript import fetch_youtube_transcript
from utils.webpage_scraper import scrape_website_text

st.set_page_config(page_title="Insight Summarizer", layout="centered")
st.title("📄 Insight Summarizer")
st.markdown("Summarize PDFs, YouTube videos, and webpages with AI")

# PDF Upload
st.subheader("📤 Upload a PDF File")
uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.info("Extracting content from PDF...")
    chunks = load_pdf("temp.pdf")
    summary = summarize_chunks(chunks)
    st.subheader("📝 Summary")
    st.write(summary)

# Divider
st.markdown("---")

# URL Input
st.subheader("🌐 Summarize a YouTube or Web Article")
url = st.text_input("Paste YouTube or article/blog URL")

if url:
    with st.spinner("Fetching content..."):
        if "youtube.com" in url or "youtu.be" in url:
            try:
                transcript = fetch_youtube_transcript(url)
                summary = summarize_chunks([transcript])
                st.subheader("📝 Video Summary")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            try:
                text = scrape_website_text(url)
                summary = summarize_chunks([text])
                st.subheader("📝 Webpage Summary")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
