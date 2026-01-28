import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Model Evaluation")

st.subheader("Actual vs Predicted Sentiment")

# Dummy Confusion Matrix
confusion_matrix = np.array([
    [8800, 100, 100],
    [150, 840, 10],
    [12, 10, 780]
])

labels = ["Neutral", "Negative", "Positive"]
normalized_cm = confusion_matrix / confusion_matrix.sum(axis=1)[:, None]

fig, ax = plt.subplots()
sns.heatmap(
    normalized_cm,
    annot=True,
    fmt=".2f",
    cmap="Greens",
    xticklabels=labels,
    yticklabels=labels,
    ax=ax
)

ax.set_xlabel("Predicted Sentiment")
ax.set_ylabel("Actual Sentiment")
ax.set_title("Confusion Matrix (Normalized)")
st.pyplot(fig)

