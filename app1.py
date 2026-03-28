import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')

st.title("🧠 AI News Bias Detector")

# Input box
news_text = st.text_area("Paste News Article Here")

def detect_bias(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.3:
        return "Positive Bias", sentiment
    elif sentiment < -0.3:
        return "Negative Bias", sentiment
    else:
        return "Neutral", sentiment

# Button
if st.button("Analyze"):
    if news_text.strip() == "":
        st.warning("Please enter text")
    else:
        bias, score = detect_bias(news_text)
        st.write("### Result")
        st.write("Bias:", bias)
        st.write("Score:", score)
        st.sidebar.title("About")
st.sidebar.info("This app detects bias using AI")

st.progress(50)