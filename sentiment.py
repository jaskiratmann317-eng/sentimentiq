from nltk.sentiment.vader import SentimentIntensityAnalyzer

# uses VADER to score the text and return a sentiment label
def get_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    # compound score ranges from -1 (most negative) to 1 (most positive)
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'

    return label, scores
