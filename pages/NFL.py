import streamlit as st
from data_integrations.odds_api import get_real_odds
from edge_legend import show_edge_legend
from predictive_models.model_manager import get_elo

show_edge_legend()

st.title("🏈 NFL - Peabody/Walters Model")

# Simulated team power ratings
TEAM_POWER = {
    "Chiefs": 5.8,
    "49ers": 6.1,
    "Bills": 4.9,
    "Eagles": 5.5,
    "Cowboys": 4.8,
    "Ravens": 5.3,
    "Dolphins": 4.7,
    "Texans": 3.9,
    "Packers": 4.2,
    "Lions": 4.6
}

def true_line(team_a, team_b):
    diff = TEAM_POWER.get(team_a, 0) - TEAM_POWER.get(team_b, 0)
    return round(diff * 1.5, 1)  # approx. 1.5 pts per power diff

def win_probability(team_a, team_b):
    rating_a = get_elo(team_a)
    rating_b = get_elo(team_b)
    elo_prob = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    return round(elo_prob, 3)

def implied_prob(odds):
    return round(100 / (abs(odds) + 100), 3) if odds > 0 else round(abs(odds) / (abs(odds) + 100), 3)

odds = get_real_odds(sport="americanfootball_nfl", market="h2h,spreads,totals")

if isinstance(odds, list):
    for game in odds[:5]:
        team_a = game["away_team"]
        team_b = game["home_team"]
        st.subheader(f"{team_a} @ {team_b}")

        book = game.get("bookmakers", [{}])[0]
        st.write(f"Bookmaker: {book.get('title', 'N/A')}")

        lines = {"h2h": {}, "spreads": {}, "totals": {}}
        for market in book.get("markets", []):
            for outcome in market["outcomes"]:
                lines[market["key"]][outcome["name"]] = outcome["price"]

        prob_a = win_probability(team_a, team_b)
        prob_b = 1 - prob_a
        impl_a = implied_prob(lines['h2h'].get(team_a, -110))
        impl_b = implied_prob(lines['h2h'].get(team_b, -110))
        edge_a = round((prob_a - impl_a) * 100, 2)
        edge_b = round((prob_b - impl_b) * 100, 2)

        line_est = true_line(team_a, team_b)
        market_spread = lines['spreads'].get(team_a, "N/A")
        spread_edge = "N/A" if isinstance(market_spread, str) else round(float(market_spread) - line_est, 1)

        st.write(f"**True Line (Power Diff):** {team_a} {line_est:+}")
        st.write(f"**Market Spread:** {team_a} {market_spread}")
        st.write(f"**Spread Edge:** {spread_edge}")

        st.markdown(f"- **{team_a}** ML: {lines['h2h'].get(team_a)} | Model: {int(prob_a*100)}% | Edge: {edge_a}%")
        st.markdown(f"- **{team_b}** ML: {lines['h2h'].get(team_b)} | Model: {int(prob_b*100)}% | Edge: {edge_b}%")

        best_bet = team_a if edge_a > edge_b else team_b
        conf = "🟢 High" if max(edge_a, edge_b) > 5 else "🟡 Medium" if max(edge_a, edge_b) > 2 else "🔴 Low"
        st.markdown(f"**Recommended Bet:** {best_bet} ML — {conf}")
        st.markdown("---")
else:
    st.error("Could not load NFL odds.")