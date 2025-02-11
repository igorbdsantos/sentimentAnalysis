from textblob import TextBlob
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('punkt')
nltk.download('wordnet')


def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    print("Sentiment Analysis")
    while True:
        text = input("Enter a feeling (or 'exit' to quit: ")
        if text.lower() == 'exit':
            break
        sentiment = analyze_sentiment(text)
        print(f"Sentiment: {sentiment}\n")

