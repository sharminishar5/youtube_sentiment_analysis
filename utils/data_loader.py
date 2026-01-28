import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_youtube_comments.csv")
    df['Cleaned_Comment'] = df['Cleaned_Comment'].fillna("")
    df['Actual_Sentiment'] = df['Actual_Sentiment'].fillna("Unknown")
    df['Comment_Length'] = df['Cleaned_Comment'].apply(len)
    return df
