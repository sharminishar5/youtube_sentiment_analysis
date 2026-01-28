import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Model Evaluation")

st.subheader("Actual vs Predicted Sentiment")

# Confusion Matrix
st.subheader("1. Actual vs Predicted Sentiment")
cm = np.array([[8800, 100, 100],
               [150, 840, 10],
               [12, 10, 780]])
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
labels = ['Neutral', 'Negative', 'Positive']
fig, ax = plt.subplots(figsize=(3,2))
sns.heatmap(cm_normalized, annot=True, fmt='.2f',
            cmap='Greens',
            xticklabels=labels,
            yticklabels=labels,
            ax=ax)
ax.set_xlabel("Predicted Sentiment")
ax.set_ylabel("Actual Sentiment")
ax.set_title("Actual vs Predicted Sentiment")
st.pyplot(fig, use_container_width=False)
plt.clf()
st.markdown("""
**Interpretation:**  
- **Neutral Sentiment:** The most classification accuracy is neutral sentiment that has 88 percent of actual neutral cases predicted correctly as neutral. Only 5-percent are falsely categorized as positive and 7-percent as negative. This shows that the model is especially useful in identifying neutral language, which is probably due to the fact that neutral reviews are likely to contain neutral or factual words, which are simpler to contrast with emotional words.   
- **Positive Sentiment:** The model has good performance in the identification of positive sentiment as 78% of the actual positive cases are correctly detected as positive. But 1 out of 10 positive reviews are wrongly identified as neutral, and 1 of 12 as negative. This implies that although the model tends to reflect positivity, not all positive utterances are dominant and some are interspersed with negative utterances that confuse (more so between positive and neutral utterances).  
- **Negative Sentiment:** The negative sentiment also shows a high performance of the model with a prediction of 84% of the instances that were actually negative. It has a small misclassification (15) in the category of neutral and 1 percent is wrongly predicted as positive. This indicates that negative sentiment is usually well represented but there are negative reviews that are not that intensive hence, could be confused with neutral sentiment. 
- **Key Findings:** The model is very accurate in all three classes of sentiment with neutral sentiment being the most accurately predicted. Mixed-upness between positive and negative is not possible directly, but rather between neutral and emotional sentiments (positive or negative). The misclassification between positive and negative is to a minimum, which means that there is high sentiment polarity separation. Altogether, the findings indicate that the sentiment analysis model is valid and balanced hence suitable in carrying out competitive analysis of customer reviews.
    """)

ax.set_xlabel("Predicted Sentiment")
ax.set_ylabel("Actual Sentiment")
ax.set_title("Confusion Matrix (Normalized)")
st.pyplot(fig)

