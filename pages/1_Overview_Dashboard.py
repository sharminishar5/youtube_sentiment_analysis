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
sentiment_counts = df['Actual_Sentiment'].value_counts()
fig, ax = plt.subplots(figsize=(3,3))
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
ax.set_title("Sentiment Percentage")
st.pyplot(fig, use_container_width=False)
plt.clf()
st.markdown("""
**Interpretation:**  
- **Neutral:**  51.6% of total comments. This is the most dominant category with more than 20000 entries. It means that most engagement of the audience is factual or informational, which may be made up of time stamps, technical queries or even broad based comments.  
- **Positive:** 38.2% of total comments. This is the second-largest segment, which represents about 15,000 instances. It indicates much community support, appreciation of the fans, and an overall positive reception of the video material.  
- **Negative:** 10.2% of total comments. This is the least amount of data that consists of approximately 4,000 comments. The low percentage implies that there is little criticism or controversy in this particular society.  
- **Key Findings:** The sentiment data indicates a vastly positive and well-being rich community environment. The neutral and positive feedback put together takes care of almost 90 percent of all interactions hence the content is effectively contributing to objective discussion and positive attitude instead of antagonism.
    """)

# WordCloud
st.subheader("3. Positive Comments WordCloud")
positive_text = " ".join(df[df['Actual_Sentiment']=="positive"]['Cleaned_Comment'])
wordcloud = WordCloud(width=350, height=180).generate(positive_text)
fig, ax = plt.subplots(figsize=(4,2))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
ax.set_title("Positive Comments WordCloud")
st.pyplot(fig, use_container_width=False)
plt.clf()
st.markdown("""
**Interpretation:**  
- **High-Intensity Appreciation:** Dominant terms such as "love," "best," "great," and "nice" confirm that the positive sentiment is driven by strong emotional satisfaction and high regard for the quality of the content.  
- **Respectful Tone:** The frequent appearance of honorifics like "sir" and "bhai" (brother), along with "thank," indicates a culture of respect and personal connection between the audience and the creator.  
- **Subject Matter Focus:** Keywords such as "video," "india," "government," and "people" suggest that positive engagement is often tied to discussions about national identity, current events, or social topics.  
- **Encouraging Feedback:** Terms like "super," "amazing," and "support" showcase an active fan base that is eager to provide motivational feedback to the creator.  
- **Key Findings:** The word cloud reveals that the community is not just "liking" the content but is deeply engaged with the specific topics presented, particularly those related to India and current affairs. The prevalence of respectful terms suggests a loyal, mature audience that views the creator as an authority or a peer.
    """)
