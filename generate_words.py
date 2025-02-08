from pytrends.request import TrendReq

# Inizializzazione
pytrends = TrendReq(hl='it', tz=360)

# Funzione per ottenere le ricerche di tendenza in Italia
def get_trending_searches():
    pytrends.build_payload(kw_list=[], geo='IT', timeframe='now 1-d')
    trending_searches = pytrends.trending_searches()
    
    # Prendi i primi 100 trend
    return trending_searches.head(100).values.flatten()

# Funzione principale
if __name__ == '__main__':
    searches = get_trending_searches()
    
    # Scrivi i risultati nel file
    with open('keywords.txt', 'w') as f:
        f.write('\n'.join(searches))
    
    print("File 'keywords.txt' aggiornato con 100 ricerche!")
