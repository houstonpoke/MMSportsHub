import requests
import os

# Make sure your Streamlit secrets or .env file contains: ODDS_API_KEY

def get_sportsbook_odds(sport_key='basketball_nba', region='us', markets='h2h,spreads,totals'):
    """
    Fetch odds from The Odds API for a given sport.
    Args:
        sport_key (str): The sport key identifier, e.g., 'basketball_nba'.
        region (str): Region to pull odds from. 'us' is standard.
        markets (str): Comma-separated markets: 'h2h', 'spreads', 'totals'.
    Returns:
        list: A list of games with odds data.
    """
    api_key = os.getenv('ODDS_API_KEY')
    if not api_key:
        raise ValueError("ODDS_API_KEY not found. Set it in your environment or Streamlit secrets.")

    url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds"
    params = {
        'apiKey': api_key,
        'regions': region,
        'markets': markets,
        'oddsFormat': 'american'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return []
