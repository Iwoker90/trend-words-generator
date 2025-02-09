from pytrends.request import TrendReq
import requests

# Inizializzazione di PyTrends
pytrends = TrendReq(hl='it', tz=360)

# Funzione per ottenere le ricerche di tendenza in Italia da PyTrends
def get_trending_searches():
    trending_searches = pytrends.trending_searches(pn='italy')
    
    # Inizializziamo una lista vuota per raccogliere tutte le tendenze
    all_trends = []
    
    # Aggiungi i primi 100 risultati (prende tutti i dati disponibili)
    all_trends.extend(trending_searches.head(100).values.flatten())
    
    print(f"PyTrends ha restituito {len(all_trends)} tendenze.")  # Log per debugging
    return all_trends[:100]  # Prendi solo i primi 100 trend

# Funzione per ottenere le parole chiave dalle notizie tramite News API
def get_trending_keywords_from_news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'it',  # Imposta il paese su Italia
        'apiKey': '1eaa205d4f1547d4b79dd2e230640f9c',  # Sostituisci con la tua chiave API
    }

    # Fai la richiesta all'API
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    # Estrai le parole chiave dai titoli delle notizie
    keywords = []
    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        keywords.extend(title.split() + description.split())

    # Prendi solo le parole uniche e limitale a 80
    unique_keywords = list(set(keywords))[:80]
    print(f"NewsAPI ha restituito {len(unique_keywords)} parole chiave.")  # Log per debugging
    return unique_keywords

# Funzione principale
if __name__ == '__main__':
    # Ottieni le tendenze da PyTrends
    searches_from_pytrends = get_trending_searches()
    
    # Ottieni le parole chiave dalle notizie
    searches_from_news = get_trending_keywords_from_news()
    
    # Unisci le due liste di tendenze
    all_searches = searches_from_pytrends + searches_from_news
    
    # Limita a 100 i risultati finali
    all_searches = all_searches[:100]
    
    # Scrivi i risultati nel file
    with open('keywords.txt', 'w') as f:
        f.write('\n'.join(all_searches))
    
    print(f"File 'keywords.txt' aggiornato con {len(all_searches)} ricerche!")
