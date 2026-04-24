SentimentIQ
C311 Programming Languages | Jaskirat Mann

DESCRIPTION
SentimentIQ analyzes user-entered text and classifies it as Positive, Negative, or Neutral using the VADER sentiment analyzer from Python's NLTK library. The web interface is built with Streamlit.

FILES
app.py           - Streamlit web interface
sentiment.py     - VADER sentiment analysis logic
requirements.txt - Project dependencies

HOW TO INSTALL
1. Clone the repo:
   git clone https://github.com/jaskiratmann317-eng/sentimentiq.git

2. Navigate into the folder:
   cd sentimentiq

3. Install dependencies:
   pip install -r requirements.txt

HOW TO RUN
streamlit run app.py

Then open your browser and go to:
http://localhost:8501

HOW TO USE
1. Type or paste any text into the input box
2. Click the Analyze button
3. The app will display the sentiment label and all four VADER scores
4. If no text is entered, a warning will appear asking you to enter some text first

EXAMPLE INPUTS AND OUTPUTS
Input:  "I absolutely love this product. Works great!"
Output: Positive | Compound: 0.8481

Input:  "This is terrible. Worst experience I have ever had."
Output: Negative | Compound: -0.8316

Input:  "The package arrived on Tuesday near the door."
Output: Neutral  | Compound: 0.0

DEPENDENCIES
Python 3, nltk, streamlit

GITHUB
https://github.com/jaskiratmann317-eng/sentimentiq.git
