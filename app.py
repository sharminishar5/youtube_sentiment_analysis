import streamlit as st
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="YouTube Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- Load Dataset ----------------
df = pd.read_csv("data/cleaned_youtube_comments.csv")

df['Cleaned_Comment'] = df['Cleaned_Comment'].fillna("")
df['Actual_Sentiment'] = df['Actual_Sentiment'].fillna("Unknown")
df['Comment_Length'] = df['Cleaned_Comment'].apply(len)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #f0f8ff;
}
.title {
    text-align: center;
    font-family: 'Arial Black', Gadget, sans-serif;
    font-size: 50px;
}
.subtitle {
    text-align: center;
    font-size: 30px;
    margin-bottom: 30px;
}
.details {
    font-size: 18px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HOME CONTENT ----------------
st.markdown('<div class="title">JIE43303 NATURAL LANGUAGE PROCESSING</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">YouTube Comments Sentiment Analysis</div>', unsafe_allow_html=True)

st.markdown("""
<div class="details">
<b>Name:</b> Sharmini A/P Selvam<br>
<b>Matric Number:</b> H22A0060<br>
<b>Scope of Topic:</b> Sentiment Analysis Dashboard<br>
<b>Dataset:</b> Kaggle<br>
<b>Dataset Link:</b>
<a href="https://www.kaggle.com/datasets/mehtaakshat/youtube-comments-data-sentiment-toxicity-spam" target="_blank">
Click Here</a>
</div>
""", unsafe_allow_html=True)

st.subheader("Dataset Preview")
st.dataframe(df.head())
