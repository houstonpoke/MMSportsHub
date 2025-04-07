import streamlit as st
import pandas as pd

st.title("💰 Bet Tracker + CLV Analysis")

if "bets" not in st.session_state:
    st.session_state.bets = []

st.subheader("➕ Add a Bet")

with st.form("add_bet_form"):
    sport = st.selectbox("Sport", ["NCAA Basketball", "NBA", "NFL", "NCAA Football", "Golf", "UFC/Boxing"])
    game = st.text_input("Matchup / Game", placeholder="e.g. Florida vs Houston")
    bet_type = st.selectbox("Bet Type", ["Moneyline", "Spread", "Over/Under"])
    odds = st.text_input("Odds (e.g. -110, +125)")
    closing_odds = st.text_input("Closing Odds (e.g. -120, +110)")
    amount = st.number_input("Wager Amount ($)", min_value=0.0, step=1.0)
    result = st.selectbox("Result", ["Pending", "Win", "Loss"])
    submit = st.form_submit_button("Add Bet")

def implied_prob(odds):
    try:
        o = int(odds)
        return round(100 / (o + 100), 3) if o > 0 else round(abs(o) / (abs(o) + 100), 3)
    except:
        return None

if submit:
    st.session_state.bets.append({
        "Sport": sport,
        "Game": game,
        "Type": bet_type,
        "Odds": odds,
        "Closing Odds": closing_odds,
        "Amount": amount,
        "Result": result
    })
    st.success("✅ Bet added with CLV.")

if st.session_state.bets:
    st.subheader("📋 Tracked Bets with CLV")
    df = pd.DataFrame(st.session_state.bets)

    def calc_clv(row):
        imp_open = implied_prob(row["Odds"])
        imp_close = implied_prob(row["Closing Odds"])
        if imp_open is not None and imp_close is not None:
            return round((imp_close - imp_open) * 100, 2)
        return None

    df["CLV (%)"] = df.apply(calc_clv, axis=1)

    def highlight_clv(val):
        if val is None:
            return ""
        elif val > 0:
            return "background-color: #d4edda"  # green
        elif val < 0:
            return "background-color: #f8d7da"  # red
        return ""

    styled_df = df.style.applymap(highlight_clv, subset=["CLV (%)"])
    st.dataframe(styled_df, use_container_width=True)

    stats = df.groupby("Type").agg({
        "Amount": "sum",
        "CLV (%)": "mean"
    }).rename(columns={"Amount": "Total Wagered", "CLV (%)": "Avg CLV (%)"})

    st.subheader("📊 Stats by Bet Type")
    st.dataframe(stats)
else:
    st.info("No bets tracked yet.")