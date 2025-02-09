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

# Funzione per ottenere i titoli dagli articoli tramite GNews API
def get_trending_keywords_from_news():
    url = 'https://gnews.io/api/v4/top-headlines'
    params = {
        'lang': 'it',  # Imposta la lingua su Italiano
        'token': '8abd8f5888fdd061cb42defea779507d',  # La tua chiave API di GNews
        'max': 100,  # Impostiamo un limite di articoli per ottenere abbastanza parole chiave
    }

    # Fai la richiesta all'API
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])

    # Estrai i titoli come singole frasi
    titles = [article.get('title', '') for article in articles]

    # Limita a 80 titoli per mantenere il file gestibile
    print(f"GNews ha restituito {len(titles)} titoli.")  # Log per debugging
    return titles[:80]

# Funzione principale
if __name__ == '__main__':
    # Ottieni le tendenze da PyTrends
    searches_from_pytrends = get_trending_searches()
    
    # Ottieni i titoli dalle notizie
    searches_from_news = get_trending_keywords_from_news()
    
    # Unisci le due liste di tendenze
    all_searches = searches_from_pytrends + searches_from_news
    
    # Se ci sono meno di 100 risultati, aggiungi articoli da GNews fino a raggiungere 100
    if len(all_searches) < 100:
        remaining = 100 - len(all_searches)
        all_searches.extend(searches_from_news[:remaining])

    # Limita a 100 i risultati finali
    all_searches = all_searches[:100]
    
    # Scrivi i risultati nel file
    with open('keywords.txt', 'w') as f:
        f.write('\n'.join(all_searches))
    
    print(f"File 'keywords.txt' aggiornato con {len(all_searches)} ricerche!")
