import streamlit as st

# Simulated fighter stats and odds
FIGHTERS = {
    "Israel Adesanya": {"elo": 1725, "str_diff": 2.1, "td_def": 80, "odds": -175},
    "Dricus Du Plessis": {"elo": 1675, "str_diff": 1.3, "td_def": 60, "odds": +145},
    "Sean O'Malley": {"elo": 1690, "str_diff": 1.9, "td_def": 72, "odds": -120},
    "Merab Dvalishvili": {"elo": 1685, "str_diff": 1.7, "td_def": 78, "odds": +100}
}

def model_win_prob(elo, str_diff, td_def):
    base = (elo - 1500) / 400
    edge = (str_diff * 10 + td_def / 5) / 100
    prob = round(min(max(base + edge, 0.05), 0.95), 3)
    return prob

def calculate_implied_probability(odds):
    return round(100 / (abs(odds) + 100), 3) if odds > 0 else round(abs(odds) / (abs(odds) + 100), 3)

st.title("🥊 UFC / Boxing - Model Predictions")

for i in range(0, len(FIGHTERS.items()), 2):
    pair = list(FIGHTERS.items())[i:i+2]
    if len(pair) < 2:
        continue

    fighter_a, stats_a = pair[0]
    fighter_b, stats_b = pair[1]

    st.subheader(f"{fighter_a} vs {fighter_b}")

    prob_a = model_win_prob(stats_a["elo"], stats_a["str_diff"], stats_a["td_def"])
    prob_b = round(1 - prob_a, 3)

    implied_a = calculate_implied_probability(stats_a["odds"])
    implied_b = calculate_implied_probability(stats_b["odds"])

    edge_a = round((prob_a - implied_a) * 100, 2)
    edge_b = round((prob_b - implied_b) * 100, 2)

    def conf_label(edge): return "🟢 High" if edge > 5 else "🟡 Medium" if edge > 2 else "🔴 Low"

    st.markdown(f"**{fighter_a}**: Odds {stats_a['odds']} | Model Win %: {int(prob_a * 100)}% | Morrow’s Edge: {edge_a}% — {conf_label(edge_a)}")
    st.markdown(f"**{fighter_b}**: Odds {stats_b['odds']} | Model Win %: {int(prob_b * 100)}% | Morrow’s Edge: {edge_b}% — {conf_label(edge_b)}")

    best_bet = fighter_a if edge_a > edge_b else fighter_b
    st.markdown(f"**Recommended Bet:** {best_bet} — {conf_label(max(edge_a, edge_b))}")
    st.markdown("---")