import streamlit as st
from predictive_models.model_manager import get_elo
from data_integrations.odds_api import get_real_odds

# Simulated player form/Elo style ratings
PLAYER_ELO = {
    "Scottie Scheffler": 1760,
    "Rory McIlroy": 1720,
    "Jon Rahm": 1740,
    "Brooks Koepka": 1700,
    "Collin Morikawa": 1685
}

FALLBACK_MARKETS = {
    "To Win": {
        "Scottie Scheffler": +400,
        "Rory McIlroy": +900,
        "Jon Rahm": +800,
        "Brooks Koepka": +2000,
        "Collin Morikawa": +3000
    },
    "Top 5": {
        "Scottie Scheffler": +140,
        "Rory McIlroy": +200,
        "Jon Rahm": +180,
        "Brooks Koepka": +500,
        "Collin Morikawa": +600
    },
    "Top 10": {
        "Scottie Scheffler": -120,
        "Rory McIlroy": +110,
        "Jon Rahm": +100,
        "Brooks Koepka": +300,
        "Collin Morikawa": +350
    }
}

def model_win_prob(player):
    base = PLAYER_ELO.get(player, 1600)
    max_rating = max(PLAYER_ELO.values())
    prob = round((base - 1500) / (max_rating - 1500), 3)
    return min(max(prob, 0.01), 0.25)

def calculate_implied_probability(odds):
    return round(100 / (abs(odds) + 100), 3) if odds > 0 else round(abs(odds) / (abs(odds) + 100), 3)

st.title("⛳ The Masters — Advanced Golf Model")

for market, players in FALLBACK_MARKETS.items():
    st.header(f"🏌️ {market} Market")
    for player, odds in players.items():
        implied = calculate_implied_probability(odds)

        # Adjust model win prob for Top 5/10
        model_prob = model_win_prob(player)
        if market == "Top 5":
            model_prob = min(model_prob * 2.1, 0.5)
        elif market == "Top 10":
            model_prob = min(model_prob * 3.5, 0.75)

        edge = round((model_prob - implied) * 100, 2)
        confidence = "🟢 High" if edge > 5 else "🟡 Medium" if edge > 2 else "🔴 Low"

        st.subheader(player)
        st.write(f"Odds: {odds}")
        st.write(f"Implied Probability: {int(implied * 100)}%")
        st.write(f"Model Probability: {int(model_prob * 100)}%")
        st.write(f"💡 Morrow’s Edge: {edge}% — {confidence}")
        st.markdown(f"**Recommendation:** {'Bet' if edge > 2 else 'Avoid'} — {confidence}")
        st.markdown("---")