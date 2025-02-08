import requests

def get_trending_keywords():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'apiKey': '1eaa205d4f1547d4b79dd2e230640f9c',
    }
    response = requests.get(url, params=params)
    articles = response.json()['articles']

    # Estrai le parole più ricercate dai titoli e descrizioni
    keywords = []
    for article in articles:
        title = article['title']
        description = article.get('description', '')
        keywords.extend(title.split() + description.split())

    # Prendi solo le prime 30 parole uniche
    unique_keywords = list(set(keywords))[:30]
    return unique_keywords

if __name__ == '__main__':
    keywords = get_trending_keywords()
    with open('keywords.txt', 'w') as f:
        f.write('\n'.join(keywords))
    print("File 'keywords.txt' aggiornato!")
