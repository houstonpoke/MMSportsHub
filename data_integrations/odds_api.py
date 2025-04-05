
import requests

API_KEY = "1a7dd942e4119ae3247632e1773aaefb"

def get_real_odds(sport="basketball_nba", region="us", market="h2h,spreads,totals"):
    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds"
    params = {
        "apiKey": API_KEY,
        "regions": region,
        "markets": market,
        "oddsFormat": "american"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}
