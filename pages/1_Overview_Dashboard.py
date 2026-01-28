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
st.subheader("1. Predicted Sentiment Distribution")
    fig, ax = plt.subplots(figsize=(3,2))
    sns.countplot(data=df, x='Actual_Sentiment', ax=ax)
    ax.set_title("Predicted Sentiment Distribution")
    st.pyplot(fig, use_container_width=False)
    plt.clf()
    st.markdown("""
**Interpretation:**  
- **Neutral (21,000+ comments):** This is the most common feeling, which means that one of the greatest parts of the audience is interested in non-emotional interactions such as timestamps, technical questions, or information sharing.  
- **Positive (around 15,000 comments):** This classification demonstrates a very good secondary wave of interaction which is community support, admiration of the creator and the overall assent to what the video is saying. 
- **Negative (around 4,000 comments):** This is the smallest sample by far which implies that the rate of friction or controversy regarding the video material is very low among the audience.
- **Key Findings:** The data shows the overwhelmingly healthy community surroundings. Due to the overwhelming number of neutral and positive comments in comparison with negative ones, the content is presented as being well-received and useful in promoting objective discussion, as opposed to conflict.
    """)

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
