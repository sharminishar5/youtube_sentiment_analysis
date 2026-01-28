import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from utils.data_loader import load_data

df = load_data()

st.header("Overview Dashboard")

# 1. Sentiment Distribution
st.subheader("1. Sentiment Distribution")
fig, ax = plt.subplots()
sns.countplot(data=df, x="Actual_Sentiment", ax=ax)
ax.set_title("Sentiment Distribution")
st.pyplot(fig)
plt.clf()

# 2. Sentiment Percentage
st.subheader("2. Sentiment Percentage")
sentiment_counts = df["Actual_Sentiment"].value_counts()

fig, ax = plt.subplots()
ax.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.axis("equal")
st.pyplot(fig)
plt.clf()

# 3. Word Cloud
st.subheader("3. Word Cloud (Positive Comments)")
positive_text = " ".join(
    df[df["Actual_Sentiment"] == "positive"]["Cleaned_Comment"]
)

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(positive_text)

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

