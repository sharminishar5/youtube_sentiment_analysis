import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from utils.data_loader import load_data

df = load_data()

st.header("Text Analysis")

# 1. Comment Length Distribution
st.subheader("1. Comment Length Distribution by Sentiment")
fig, ax = plt.subplots(figsize=(3,2))
sns.boxplot(data=df, x='Actual_Sentiment', y='Comment_Length', ax=ax)
ax.set_title("Comment Length Distribution by Sentiment")
st.pyplot(fig, use_container_width=False)
plt.clf()
st.markdown("""
**Interpretation:**  
- **Neutral:** These are the most brief and minimally written comments. The tight and low median means that neutral engagement is usually comprised of very brief and functional text.
- **Positive:** Although most of the positive comments are concise, this undertaking has the largest number of extreme outliers. Other fans are extremely outspoken, and single appreciative messages can go as long as 4,500 characters.
- **Negative:** This group is the longest medians with a broader distribution than the rest. It implies that whenever the viewers are dissatisfied or have a complaint or a critique, he or she resorts to writing lengthy and elaborate responses to argue his or her point of view.
- **Key Findings:** The results indicate that there is a strong correlation between sentiment and verbosity. Although the society at large favors the brief, negative criticisms are usually more detailed compared to positive ones. The extreme outliers in the positive category indicate the existence of a small yet loyal group of the audience that composes long-form supportive content.
    """)

# 2. Top Words in Positive Comments
st.subheader("2. Top Words in Positive Comments")
positive_words = " ".join(df[df['Actual_Sentiment']=="positive"]['Cleaned_Comment']).split()
pos_freq = Counter(positive_words).most_common(10)
words = [w[0] for w in pos_freq]
counts = [w[1] for w in pos_freq]
fig, ax = plt.subplots(figsize=(3,2))
sns.barplot(x=counts, y=words, ax=ax)
ax.set_title("Top Words in Positive Comments")
st.pyplot(fig, use_container_width=False)
plt.clf()
st.markdown("""
**Interpretation:**  
- **Core sentiment:** The highest-ranking words, "good," "love," and "best," confirm that the majority of positive feedback is centered around general satisfaction and high-quality praise for the content.  
- **Engagement:** The high frequency of the word "please" suggests that even within positive comments, the audience is actively engaging by making requests for future content or specific shout-outs.
- **Creator Audience Connection:** Terms like "sir," "bro," and "hai" (a common greeting) highlight a personal and respectful connection between the viewers and the creator. 
- **Topic relevance:** The appearance of "India" and "video" indicates that the positive sentiment is specifically tied to the video's subject matter or national pride. 
- **Key Findings:** The positive engagement is not just emotional but also conversational. Viewers aren't just saying they like the video; they are using respectful language to build a relationship with the creator and are actively participating in the channel's growth through suggestions and requests.
    """)

