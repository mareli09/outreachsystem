from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(feedback):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(feedback)['compound']
    return score
