import streamlit as st
import nltk
from sentiment import get_sentiment

# download the VADER lexicon if not already present
nltk.download('vader_lexicon', quiet=True)

st.title('SentimentIQ')
st.write('Enter a sentence, review, or social media post to analyze its sentiment.')

text = st.text_area('Input Text', height=150)

if st.button('Analyze'):
    if text.strip() == '':
        st.warning('Please enter some text first.')
    else:
        label, scores = get_sentiment(text)

        st.subheader('Result')
        st.write('Sentiment:', label)

        # show the individual VADER scores so the user can see the breakdown
        st.write('Positive score:', scores['pos'])
        st.write('Negative score:', scores['neg'])
        st.write('Neutral score:', scores['neu'])
        st.write('Compound score:', scores['compound'])
