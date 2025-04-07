import streamlit as st
import requests

# Securely get your API key from .streamlit/secrets.toml
RAPIDAPI_KEY = st.secrets["RAPIDAPI_KEY"]
BASE_URL = "https://sportsbook-api2.p.rapidapi.com"

HEADERS = {
    "x-rapidapi-host": "sportsbook-api2.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY
}

def get_sportsbook_odds(market_type="ARBITRAGE", league="NBA"):
    url = f"{BASE_URL}/v0/advantages/?type={market_type}&league={league.upper()}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed with status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}