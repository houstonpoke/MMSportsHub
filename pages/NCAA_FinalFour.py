import streamlit as st
from predictive_models.model_manager import win_probability

games = [
    {"team_a": "Florida", "team_b": "Auburn", "line": -2, "total": 158.5, "team_totals": {"Florida": 80.5, "Auburn": 78.5}},
    {"team_a": "Duke", "team_b": "Houston", "line": -5, "total": 136.5, "team_totals": {"Duke": 70.5, "Houston": 66}}
]

def implied_prob_from_odds(odds):
    if odds > 0:
        return round(100 / (odds + 100), 2)
    else:
        return round(abs(odds) / (abs(odds) + 100), 2)

st.title("🏀 NCAA Final Four - Model Predictions")

for game in games:
    team_a = game["team_a"]
    team_b = game["team_b"]
    st.subheader(f"{team_a} vs {team_b}")

    prob, elo_a, elo_b = win_probability(team_a, team_b)
    prob_b = round(1 - prob, 3)
    edge_a = round((prob - 0.5) * 100, 1)
    edge_b = -edge_a

    st.markdown(f"**Model Win Probability**")
    st.write(f"{team_a}: {int(prob*100)}% | {team_b}: {int(prob_b*100)}%")
    st.write(f"Elo Ratings: {team_a} {elo_a} vs {team_b} {elo_b}")

    st.markdown("**Spread Analysis**")
    model_line = round((elo_a - elo_b) / 25, 1)
    spread_edge = game['line'] - model_line
    pick = team_b if spread_edge > 0 else team_a
    st.write(f"Market Spread: {team_a} {game['line']:+}")
    st.write(f"Model Spread: {team_a} {model_line:+}")
    st.write(f"📣 **Recommendation:** Bet {pick} Spread")

    st.markdown("**Total Analysis**")
    st.write(f"Market Total: {game['total']} pts")
    st.write("Model Total: Coming soon...")

    st.markdown("**Team Totals**")
    for team, total in game["team_totals"].items():
        st.write(f"{team}: o/u {total} — Model: Coming soon...")

    st.markdown("---")