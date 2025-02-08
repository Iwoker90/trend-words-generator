import requests

def get_trending_keywords():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'it',  # Cambiato da 'us' a 'it' per le notizie italiane
        'apiKey': '1eaa205d4f1547d4b79dd2e230640f9c',
    }
    response = requests.get(url, params=params)
    articles = response.json()['articles']

    # Estrai le parole più ricercate dai titoli e descrizioni
    keywords = []
    for article in articles:
        title = article['title']
        description = article.get('description', '')  # Usa una stringa vuota se 'description' è None

        # Verifica che la description non sia None
        keywords.extend(title.split() + (description.split() if description else []))

    # Prendi solo le prime 30 parole uniche
    unique_keywords = list(set(keywords))[:30]
    return unique_keywords

if __name__ == '__main__':
    keywords = get_trending_keywords()
    with open('keywords.txt', 'w') as f:  # Manteniamo il nome 'keywords.txt'
        f.write('\n'.join(keywords))
    print("File 'keywords.txt' aggiornato!")
