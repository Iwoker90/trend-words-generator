import requests
import json
import random

def get_trending_words():
    """Ottiene solo le parole chiave dalle tendenze del giorno."""
    url = "https://trends.google.com/trends/api/dailytrends?geo=US"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text[5:])  # Rimuove caratteri iniziali inutili
        trends = data.get("default", {}).get("trendingSearchesDays", [])
        
        words = []
        for day in trends:
            for trend in day.get("trendingSearches", []):
                words.append(trend.get("query", ""))  # Prende solo il titolo della tendenza
        
        return [word for word in words if word]  # Rimuove eventuali stringhe vuote
    
    return []

def generate_file():
    """Genera un file con 100 parole casuali dalle tendenze e le salva come lista JSON."""
    words = get_trending_words()
    if not words:
        words = ["nessuna", "tendenza", "disponibile"]
    
    selected_words = random.sample(words, min(100, len(words)))  # Evita duplicati
    
    with open("words.txt", "w") as f:
        json.dump(selected_words, f, ensure_ascii=False, indent=2)  # Salva in formato lista JSON

if __name__ == "__main__":
    generate_file()
