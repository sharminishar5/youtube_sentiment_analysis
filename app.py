import streamlit as st

st.set_page_config(
    page_title="YouTube Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("📊 Navigation")

st.title("YouTube Comments Sentiment Analysis Dashboard")
st.markdown("""
This dashboard presents a **sentiment analysis of YouTube comments**  
using Natural Language Processing (NLP).

👉 Please select a page from the sidebar to begin.
""")
