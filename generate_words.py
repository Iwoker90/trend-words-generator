import requests

def get_trending_keywords():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'apiKey': 'YOUR_NEWSAPI_KEY',  # Sostituisci con la tua chiave API
    }
    response = requests.get(url, params=params)
    
    print("Status code:", response.status_code)  # Mostra il codice di stato
    print("Response JSON:", response.json())  # Mostra la risposta JSON per il debug

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
    
    # Debug per vedere le parole estratte
    print("Keywords:", unique_keywords)
    
    # Salva nel file
    with open('words.txt', 'w') as file:
        file.write('\n'.join(unique_keywords))  # Scrive le parole nel file
    return unique_keywords

get_trending_keywords()
