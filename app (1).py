# pip install transformers
# pip install streamlit
# pip install torch

import streamlit as st
from transformers import pipeline

# Title for the app
st.title('Sentiment Analysis Bot')

# Load sentiment-analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Text input for the user
user_text = st.text_input("Enter a sentence to analyze its sentiment")

# Button to trigger sentiment analysis
if st.button("Analyze Sentiment"):
    # Get sentiment
    result = sentiment_analyzer(user_text)[0]

    # Display the result
    label = result['label']
    score = round(result['score'], 4)
    
    st.subheader("Sentiment Result:")
    st.write(f"Sentiment: **{label}**")
    st.write(f"Confidence Score: **{score}**")
