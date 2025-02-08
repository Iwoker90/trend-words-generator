import requests
import nltk

# Scarica risorse necessarie per ngrams
nltk.download('punkt')

# Funzione per ottenere i titoli principali delle notizie italiane
def get_trending_titles():
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

    # Estrai i titoli principali delle notizie
    titles = []
    for article in articles:
        title = article['title']
        
        # Filtra i titoli che sono solo "Google News" o troppo generici
        if title and "Google News" not in title and len(title.split()) > 3:
            titles.append(title)

    return titles

if __name__ == '__main__':
    titles = get_trending_titles()

    # Se non sono stati trovati titoli, stampa un messaggio
    if not titles:
        print("Nessun titolo trovato.")
    else:
        with open('keywords.txt', 'w') as f:
            f.write('\n'.join(titles))
        print("File 'keywords.txt' aggiornato con i titoli principali!")
