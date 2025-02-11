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
        return "Positivo"
    elif polarity < 0:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    print("Analisador de Sentimentos")
    while True:
        text = input("Digite um texto (ou 'sair' para encerrar): ")
        if text.lower() == 'sair':
            break
        sentiment = analyze_sentiment(text)
        print(f"Sentimento: {sentiment}\n")

