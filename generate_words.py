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
                words.append(trend.get("title", ""))  # Prende solo il titolo della tendenza
        
        return [str(word) for word in words if word]  # Assicura che siano solo stringhe
    
    return []

def generate_file():
    """Genera un file con 100 parole casuali dalle tendenze."""
    words = get_trending_words()
    if not words:
        words = ["nessuna", "tendenza", "disponibile"]
    
    selected_words = random.choices(words, k=min(100, len(words)))  # Evita errori se ci sono meno di 100 parole
    
    with open("words.txt", "w") as f:
        f.write(" ".join(selected_words))

if __name__ == "__main__":
    generate_file()

