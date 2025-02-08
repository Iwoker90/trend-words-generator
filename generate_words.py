def get_trending_keywords():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'apiKey': 'YOUR_NEWSAPI_KEY',
    }
    response = requests.get(url, params=params)

    # Stampa la risposta completa per il debug
    print(response.json())  # Aggiungi questa riga per esaminare la risposta

    # Controlla se la chiave 'articles' è presente
    if 'articles' not in response.json():
        print("Errore: La risposta non contiene 'articles'. Verifica la tua API key o la risposta dell'API.")
        return []

    articles = response.json()['articles']
    keywords = []
    for article in articles:
        title = article['title']
        description = article.get('description', '')
        keywords.extend(title.split() + description.split())

    # Prendi solo le prime 30 parole uniche
    unique_keywords = list(set(keywords))[:30]
    return unique_keywords
