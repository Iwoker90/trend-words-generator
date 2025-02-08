import requests
import json

def get_trending_words():
    """Ottiene solo le parole chiave dalle tendenze del giorno."""
    url = "https://trends.google.com/trends/api/dailytrends?geo=US"
    response = requests.get(url)

    print("STATUS CODE:", response.status_code)  # Debug

    if response.status_code == 200:
        try:
            # Proviamo a rimuovere i caratteri iniziali che non sono parte del JSON
            raw_data = response.text[5:]  # Rimuove ')]}' per ottenere il JSON corretto
            
            print("RAW DATA:", raw_data[:500])  # Stampa i primi 500 caratteri della risposta

            data = json.loads(raw_data)
            trends = data.get("default", {}).get("trendingSearchesDays", [])
            
            words = []
            for day in trends:
                for trend in day.get("trendingSearches", []):
                    query = trend.get("query", "")
                    if query:
                        words.append(query)
            
            print("PAROLE TROVATE:", words)  # Debug
            return words if words else ["Nessuna tendenza disponibile"]
        
        except Exception as e:
            print("ERRORE NEL PARSING JSON:", str(e))
            return ["Errore nel parsing dei dati"]
    
    return ["Errore nella richiesta API"]

if __name__ == "__main__":
    get_trending_words()
