import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(layout="wide")

df = pd.read_csv("cleaned_youtube_comments.csv")
df['Cleaned_Comment'] = df['Cleaned_Comment'].fillna("")
df['Actual_Sentiment'] = df['Actual_Sentiment'].fillna("Unknown")

st.title("📊 Overview Dashboard")

# Sentiment Distribution
st.subheader("1. Sentiment Distribution")
fig, ax = plt.subplots(figsize=(4,3))
sns.countplot(data=df, x='Actual_Sentiment', ax=ax)
st.pyplot(fig)
plt.clf()

# Sentiment Percentage
st.subheader("2. Sentiment Percentage")
counts = df['Actual_Sentiment'].value_counts()
fig, ax = plt.subplots()
ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
st.pyplot(fig)
plt.clf()

# WordCloud
st.subheader("3. Positive Comments WordCloud")
text = " ".join(df[df['Actual_Sentiment']=="positive"]['Cleaned_Comment'])
wc = WordCloud(width=500, height=300).generate(text)
fig, ax = plt.subplots()
ax.imshow(wc)
ax.axis("off")
st.pyplot(fig)
