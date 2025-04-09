# 📁 sportsbook_api.py

import requests
import os

ODDS_API_KEY = os.getenv('ODDS_API_KEY')  # Make sure this is set in your Streamlit secrets

def get_sportsbook_odds(sport_key='basketball_nba', region='us', markets='h2h,spreads,totals'):
    url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds"
    params = {
        'apiKey': ODDS_API_KEY,
        'regions': region,
        'markets': markets,
        'oddsFormat': 'american'
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching odds: {response.status_code} - {response.text}")
        return []

    return response.json()
