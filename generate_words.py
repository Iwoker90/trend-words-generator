import requests
import json

def get_trending_words():
    """Ottiene solo le parole chiave dalle tendenze del giorno."""
    url = "https://trends.google.com/trends/api/dailytrends?geo=US"
    response = requests.get(url)

    print("STATUS CODE:", response.status_code)  # Debug

    if response.status_code == 200:
        print("RAW RESPONSE:", response.text[:500])  # Debug: Mostra i primi 500 caratteri della risposta
        
        try:
            data = json.loads(response.text[5:])  # Rimuove caratteri iniziali inutili
            trends = data.get("default", {}).get("trendingSearchesDays", [])
            
            words = []
            for day in trends:
                for trend in day.get("trendingSearches", []):
                    words.append(trend.get("query", ""))  # Prende solo il titolo della tendenza
            
            print("PAROLE TROVATE:", words)  # Debug
            return [word for word in words if word]  # Rimuove eventuali stringhe vuote
        
        except Exception as e:
            print("ERRORE JSON:", str(e))
            return []

    return []

if __name__ == "__main__":
    get_trending_words()

