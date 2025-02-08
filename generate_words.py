import requests
import json
import random

def get_trending_words():
    """Ottiene le parole chiave dalle tendenze del giorno."""
    url = "https://trends.google.com/trends/api/dailytrends?geo=US"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text[5:])  # Rimuove caratteri iniziali inutili
        trends = data.get("default", {}).get("trendingSearchesDays", [])
        
        words = []
        for day in trends:
            for trend in day.get("trendingSearches", []):
                # Aggiungiamo solo il titolo (la stringa della tendenza)
                words.append(trend.get("query", ""))
        
        return words
    return []

def generate_file():
    """Genera un file con 100 parole casuali dalle tendenze."""
    words = get_trending_words()
    if not words:
        words = ["nessuna", "tendenza", "disponibile"]
    
    selected_words = random.choices(words, k=100)
    
    with open("words.txt", "w") as f:
        # Scriviamo ogni parola su una nuova riga
        f.write("\n".join(selected_words))  # Parole separati da una nuova riga

if __name__ == "__main__":
    generate_file()
