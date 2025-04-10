import streamlit as st
from data_integrations.odds_api import get_real_odds
from predictive_models.model_manager import win_probability
from edge_legend import show_edge_legend

show_edge_legend()

def calculate_implied_probability(odds):
    return round(100 / (abs(odds) + 100), 3) if odds > 0 else round(abs(odds) / (abs(odds) + 100), 3)

def analyze_market(market_key, outcomes, team_a, team_b):
    st.write(f"### 📈 {market_key.upper()} Odds & Analysis")
    for outcome in outcomes:
        name = outcome['name']
        price = outcome['price']
        implied = calculate_implied_probability(price)
        model_win_prob, elo_a, elo_b = win_probability(team_a, team_b)
        actual_model_win_prob = model_win_prob if name == team_a else 1 - model_win_prob
        morrows_edge = round((actual_model_win_prob - implied) * 100, 2)
        confidence = "🟢 High" if morrows_edge > 5 else "🟡 Medium" if morrows_edge > 2 else "🔴 Low"

        st.markdown(f"**{name}**: {price} (Implied Win %: {int(implied * 100)}%)")
        st.markdown(f"- Model Win %: {int(actual_model_win_prob * 100)}%")
        st.markdown(f"- Elo Ratings: {elo_a} vs {elo_b}")
        st.markdown(f"- 💡 Morrow's Edge: {morrows_edge}% — {confidence}")
        st.markdown(f"**Recommendation:** Bet {name} ({market_key.upper()}) — {confidence}")
        st.markdown("---")

st.title("🏀 NCAA Basketball - MM Sports Hub")

odds = get_real_odds(sport="basketball_ncaab", market="h2h,spreads,totals")
if isinstance(odds, list):
    for game in odds[:3]:
        team_a = game["away_team"]
        team_b = game["home_team"]
        st.subheader(f"{team_a} @ {team_b}")
        if game.get('bookmakers'):
            book = game['bookmakers'][0]
            st.write(f"Bookmaker: {book['title']}")
            for market in book['markets']:
                analyze_market(market['key'], market['outcomes'], team_a, team_b)
else:
    st.error("Failed to load NCAA Basketball odds.")