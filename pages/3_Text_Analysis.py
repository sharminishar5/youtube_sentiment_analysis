import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from utils.data_loader import load_data

df = load_data()

st.header("Text Analysis")

# 1. Comment Length Distribution
st.subheader("1. Comment Length Distribution by Sentiment")

fig, ax = plt.subplots()
sns.boxplot(
    data=df,
    x="Actual_Sentiment",
    y="Comment_Length",
    ax=ax
)
ax.set_title("Comment Length vs Sentiment")
st.pyplot(fig)
plt.clf()

# 2. Top Words in Positive Comments
st.subheader("2. Top Words in Positive Comments")

positive_words = " ".join(
    df[df["Actual_Sentiment"] == "positive"]["Cleaned_Comment"]
).split()

top_words = Counter(positive_words).most_common(10)

words = [w[0] for w in top_words]
counts = [w[1] for w in top_words]

fig, ax = plt.subplots()
sns.barplot(x=counts, y=words, ax=ax)
ax.set_title("Top 10 Words in Positive Comments")
st.pyplot(fig)

