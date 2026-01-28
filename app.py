import streamlit as st

st.set_page_config(
    page_title="YouTube Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Overview Dashboard", "Text Analysis", "Model Evaluation"])

# ---------------- Load Dataset ----------------
df = pd.read_csv("cleaned_youtube_comments.csv")

# Fill missing values
df['Cleaned_Comment'] = df['Cleaned_Comment'].fillna("")
df['Actual_Sentiment'] = df['Actual_Sentiment'].fillna("Unknown")
df['Comment_Length'] = df['Cleaned_Comment'].apply(len)

# ---------------- Custom CSS for background and fonts ----------------
st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #f0f8ff;  /* Light blue background */
    }

    /* Title and subtitle */
    .title {
        text-align: center;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 50px;
        color: #1a1a1a;
    }
    .subtitle {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 30px;
        color: #333333;
        margin-bottom: 30px;
    }

    /* Details text */
    .details {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #000000;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True
)

# ---------------- Page 1: Home / Cover Page ----------------
if page == "Home":
    st.markdown('<div class="title">JIE43303 NATURAL LANGUAGE PROCESSING</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">YouTube Comments Sentiment Analysis</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="details">
    <b>Name:</b> Sharmini A/P Selvam<br>
    <b>Matric Number:</b> H22A0060<br>
    <b>Scope of Topic:</b> Sentiment Analysis Dashboard<br>
    <b>Dataset:</b> Kaggle<br>
    <b>Dataset Link:</b> <a href="https://www.kaggle.com/datasets/mehtaakshat/youtube-comments-data-sentiment-toxicity-spam?utm_source=chatgpt.com" target="_blank">Click Here</a>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())
