import subprocess
import sys

# Funzione per installare pytrends se non è già installato
def install_pytrends():
    try:
        import pytrends
    except ImportError:
        print("pytrends non trovato, installazione in corso...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytrends"])

# Installiamo pytrends se necessario
install_pytrends()

from pytrends.request import TrendReq

# Inizializza pytrends
pytrends = TrendReq(hl='it', tz=360)

# Funzione per ottenere le tendenze di ricerca in Italia
def get_trending_searches():
    pytrends.build_payload(kw_list=[], geo='IT', timeframe='now 1-d')
    trending_searches = pytrends.trending_searches(pn='italy')  # Prendi le tendenze di ricerca in Italia
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
