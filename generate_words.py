import requests

def get_trending_keywords():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'it',  # Italia
        'apiKey': '1eaa205d4f1547d4b79dd2e230640f9c',
    }
    response = requests.get(url, params=params)

    # Verifica della risposta dell'API
    if response.status_code != 200:
        print(f"Errore nella richiesta: {response.status_code}")
        return []

    data = response.json()

    # Verifica se la chiave 'articles' è presente e se contiene articoli
    if 'articles' not in data or not data['articles']:
        print("Nessun articolo trovato.")
        return []

    articles = data['articles']

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

    # Se non sono state trovate parole, stampa un messaggio
    if not keywords:
        print("Nessuna parola trovata.")
    else:
        with open('keywords.txt', 'w') as f:
            f.write('\n'.join(keywords))
        print("File 'keywords.txt' aggiornato!")
