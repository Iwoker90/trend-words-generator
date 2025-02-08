from pytrends.request import TrendReq

# Inizializzazione
pytrends = TrendReq(hl='it', tz=360)

# Funzione per ottenere le ricerche di tendenza in Italia
def get_trending_searches():
    trending_searches = pytrends.trending_searches(pn='italy')
    
    # Inizializziamo una lista vuota per raccogliere tutte le tendenze
    all_trends = []
    
    # Aggiungi i primi 20 risultati
    all_trends.extend(trending_searches.head(20).values.flatten())
    
    # Proviamo a ottenere altri 80 (in gruppi da 20)
    for i in range(1, 5):  # Aggiungi 4 richieste per ottenere altre 80 tendenze
        start = i * 20
        all_trends.extend(trending_searches.iloc[start:start+20].values.flatten())
    
    return all_trends[:100]  # Prendi solo i primi 100 trend

# Funzione principale
if __name__ == '__main__':
    searches = get_trending_searches()
    
    # Scrivi i risultati nel file
    with open('keywords.txt', 'w') as f:
        f.write('\n'.join(searches))
    
    print("File 'keywords.txt' aggiornato con 100 ricerche!")
