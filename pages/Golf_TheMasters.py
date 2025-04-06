import streamlit as st
from predictive_models.model_manager import get_elo
from data_integrations.odds_api import get_real_odds

# Simulated Masters player Elo-like form ratings
PLAYER_ELO = {
    "Scottie Scheffler": 1760,
    "Rory McIlroy": 1720,
    "Jon Rahm": 1740,
    "Brooks Koepka": 1700,
    "Collin Morikawa": 1685
}

def model_win_prob(player):
    base = PLAYER_ELO.get(player, 1600)
    max_rating = max(PLAYER_ELO.values())
    prob = round((base - 1500) / (max_rating - 1500), 3)
    return min(max(prob, 0.01), 0.25)  # cap at 25%

def calculate_implied_probability(odds):
    return round(100 / (abs(odds) + 100), 3) if odds > 0 else round(abs(odds) / (abs(odds) + 100), 3)

st.title("⛳ The Masters - Model Predictions")

odds_data = get_real_odds(sport="golf_masters", market="h2h")

if isinstance(odds_data, list) and odds_data:
    shown = 0
    for book in odds_data[0].get("bookmakers", []):
        for market in book.get("markets", []):
            for outcome in market.get("outcomes", []):
                player = outcome["name"]
                odds = outcome["price"]
                implied = calculate_implied_probability(odds)
                model_prob = model_win_prob(player)
                edge = round((model_prob - implied) * 100, 2)

                confidence = "🟢 High" if edge > 5 else "🟡 Medium" if edge > 2 else "🔴 Low"

                st.subheader(player)
                st.write(f"Odds: {odds}")
                st.write(f"Implied Win %: {int(implied * 100)}%")
                st.write(f"Model Win %: {int(model_prob * 100)}%")
                st.write(f"Morrow's Edge: {edge}% — {confidence}")
                st.markdown(f"**Recommendation:** {'Bet' if edge > 2 else 'Avoid'} — {confidence}")
                st.markdown("---")

                shown += 1
                if shown >= 5:
                    break
            break
        break
else:
    st.error("Could not load Masters odds.")