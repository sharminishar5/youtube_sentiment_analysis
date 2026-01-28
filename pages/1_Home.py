import streamlit as st
from utils.data_loader import load_data

df = load_data()

st.markdown("## JIE43303 – Natural Language Processing")
st.markdown("### YouTube Comments Sentiment Analysis")

st.markdown("""
**Name:** Sharmini A/P Selvam  
**Matric Number:** H22A0060  
**Scope:** Sentiment Analysis Dashboard  
**Dataset Source:** Kaggle  
""")

st.markdown(
    "[🔗 Dataset Link](https://www.kaggle.com/datasets/mehtaakshat/youtube-comments-data-sentiment-toxicity-spam)"
)

st.subheader("Dataset Preview")
st.dataframe(df.head())
