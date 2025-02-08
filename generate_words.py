from pytrends.request import TrendReq

# Inizializza pytrends
pytrends = TrendReq(hl='it', tz=360)

# Funzione per ottenere le tendenze di ricerca in Italia
def get_trending_searches():
    trending_searches = pytrends.trending_searches(pn='italy')  # Ottieni direttamente le tendenze in Italia senza build_payload
    return trending_searches

if __name__ == '__main__':
    searches = get_trending_searches()

    # Se non sono state trovate tendenze, stampa un messaggio
    if not searches.empty:
        searches_list = searches[0].tolist()  # Converte la serie pandas in lista
        with open('keywords.txt', 'w') as f:
            f.write('\n'.join(searches_list))
        print("File 'keywords.txt' aggiornato con le tendenze di ricerca!")
    else:
        print("Nessuna tendenza di ricerca trovata.")
