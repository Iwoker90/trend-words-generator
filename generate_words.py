import requests
from collections import Counter
import string
from nltk import ngrams

# Lista di stopwords italiane (parole comuni da ignorare)
stopwords = set([
    "di", "a", "in", "e", "il", "la", "per", "con", "su", "che", "un", "una", 
    "dei", "della", "alle", "sulle", "dal", "al", "ma", "come", "è", "sono", "quello", 
    "questo", "si", "non", "perché", "l", "da", "sì", "ha", "questi", "ci", "dopo", 
    "prima", "come", "bene", "anche", "dovrebbe", "quali", "tra", "questo"
])

def get_trending_keywords():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'sources': 'google-news-it',  # Filtro per le notizie italiane di Google News
        'apiKey': '1eaa205d4f1547d4b79dd2e230640f9c',  # La tua chiave API
    }
    response = requests.get(url, params=params)

    # Verifica della risposta dell'API
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Errore nella richiesta: {response.status_code}")
        return []

    data = response.json()

    # Stampa la risposta completa per il debug
    print("Dati ricevuti:", data)

    if 'articles' not in data or not data['articles']:
        print("Nessun articolo trovato.")
        return []

    articles = data['articles']

    # Estrai le parole più significative dai titoli e descrizioni
    keywords = []
    for article in articles:
        title = article['title']
        description = article.get('description', '')  # Usa una stringa vuota se 'description' è None

        # Filtriamo e puliamo i titoli e le descrizioni dalle stopwords
        title_words = [word.lower() for word in title.split() if word.lower() not in stopwords and word not in string.punctuation]
        description_words = [word.lower() for word in description.split() if word.lower() not in stopwords and word not in string.punctuation]

        # Aggiungiamo le parole significative alla lista
        keywords.extend(title_words + description_words)

    # Estraiamo i bigrammi (combinazioni di 2 parole)
    bigrams = ngrams(keywords, 2)

    # Conta la frequenza dei bigrammi
    bigram_counts = Counter(bigrams)

    # Prendi solo i bigrammi più comuni
    unique_keywords = [' '.join(bigram) for bigram, _ in bigram_counts.most_common(30)]
    return unique_keywords

if __name__ == '__main__':
    keywords = get_trending_keywords()

    # Se non sono state trovate parole, stampa un messaggio
    if not keywords:
        print("Nessuna parola trovata.")
    else:
        with open('keywords.txt', 'w') as f:
            f.write('\n'.join(keywords))
        print("File 'keywords.txt' aggiornato!")
