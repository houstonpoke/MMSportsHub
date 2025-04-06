import streamlit as st
from predictive_models.model_manager import get_elo
from data_integrations.odds_api import get_real_odds
from edge_legend import show_edge_legend

show_edge_legend()

# Simulated dynamic Elo scores for demo
TOURNAMENTS = {
    "The Masters": {
        "Scottie Scheffler": 1760,
        "Rory McIlroy": 1720,
        "Jon Rahm": 1740,
        "Brooks Koepka": 1700,
        "Collin Morikawa": 1685
    },
    "PGA Championship": {
        "Xander Schauffele": 1705,
        "Justin Thomas": 1675,
        "Tony Finau": 1650,
        "Viktor Hovland": 1725,
        "Max Homa": 1640
    }
}

def model_win_prob(base_rating, max_rating):
    prob = round((base_rating - 1500) / (max_rating - 1500), 3)
    return min(max(prob, 0.01), 0.25)

def calculate_implied_probability(odds):
    return round(100 / (abs(odds) + 100), 3) if odds > 0 else round(abs(odds) / (abs(odds) + 100), 3)

st.title("⛳ Golf Model — Weekly Tournament View")

tournament = st.selectbox("Select Tournament", list(TOURNAMENTS.keys()))
players = TOURNAMENTS[tournament]
max_elo = max(players.values())

MARKETS = {
    "To Win": {
        player: odds for player, odds in zip(players.keys(), [400, 900, 800, 2000, 3000])
    },
    "Top 5": {
        player: odds for player, odds in zip(players.keys(), [140, 200, 180, 500, 600])
    },
    "Top 10": {
        player: odds for player, odds in zip(players.keys(), [-120, 110, 100, 300, 350])
    }
}

for market, player_odds in MARKETS.items():
    st.header(f"🏌️ {market} Market")
    for player, odds in player_odds.items():
        elo = players[player]
        base_win_prob = model_win_prob(elo, max_elo)

        if market == "Top 5":
            model_prob = min(base_win_prob * 2.1, 0.5)
        elif market == "Top 10":
            model_prob = min(base_win_prob * 3.5, 0.75)
        else:
            model_prob = base_win_prob

        implied = calculate_implied_probability(odds)
        edge = round((model_prob - implied) * 100, 2)
        confidence = "🟢 High" if edge > 5 else "🟡 Medium" if edge > 2 else "🔴 Low"

        st.subheader(player)
        st.write(f"Odds: {odds}")
        st.write(f"Implied Probability: {int(implied * 100)}%")
        st.write(f"Model Probability: {int(model_prob * 100)}%")
        st.write(f"💡 Morrow’s Edge: {edge}% — {confidence}")
        st.markdown(f"**Recommendation:** {'Bet' if edge > 2 else 'Avoid'} — {confidence}")
        st.markdown("---")
