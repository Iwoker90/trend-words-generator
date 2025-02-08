import requests
import json
import random

def get_trending_words():
    """Ottiene le parole chiave dalle tendenze del giorno."""
    url = "https://trends.google.com/trends/api/dailytrends?geo=US"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            # Rimuove caratteri iniziali inutili (se ce ne sono) e stampa la risposta grezza
            data = json.loads(response.text[5:])  # Tagliamo i primi 5 caratteri per rimuovere il prefisso
            print("Dati ricevuti dall'API:", json.dumps(data, indent=2))  # Debug: Mostriamo la risposta JSON

            trends = data.get("default", {}).get("trendingSearchesDays", [])
            print("Tendenze trovate:", trends)  # Debug: Verifica se le tendenze sono presenti

            words = []
            for day in trends:
                for trend in day.get("trendingSearches", []):
                    query = trend.get("query", "")
                    if query:
                        words.append(query)
            
            print("Parole estratte:", words)  # Debug: Vedi le parole estratte
            
            return words
        except Exception as e:
            print("Errore nel parsing dei dati:", e)
            return []
    else:
        print("Errore nella richiesta API:", response.status_code)
        return []

def generate_file():
    """Genera un file con 100 parole casuali dalle tendenze."""
    words = get_trending_words()
    if not words:
        words = ["nessuna", "tendenza", "disponibile"]
    
    selected_words = random.choices(words, k=100)
    
    with open("words.txt", "w") as f:
        f.write("\n".join(selected_words))  # Parole separati da una nuova riga

if __name__ == "__main__":
    generate_file()

