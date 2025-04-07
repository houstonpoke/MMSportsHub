import streamlit as st
import pandas as pd

st.title("💵 Bet Tracker")

# Load or initialize session state bet history
if "bets" not in st.session_state:
    st.session_state.bets = []

st.subheader("➕ Add a Bet")

with st.form("add_bet_form"):
    sport = st.selectbox("Sport", ["NCAA Basketball", "NBA", "NFL", "NCAA Football", "Golf", "UFC/Boxing"])
    game = st.text_input("Matchup / Game", placeholder="e.g. Florida vs Houston")
    bet_type = st.selectbox("Bet Type", ["Moneyline", "Spread", "Over/Under"])
    line = st.text_input("Odds / Line (e.g. -110, +3.5, O/U 141.5)")
    amount = st.number_input("Wager Amount ($)", min_value=0.0, step=1.0)
    result = st.selectbox("Result", ["Pending", "Win", "Loss"])
    submit = st.form_submit_button("Add Bet")

if submit:
    st.session_state.bets.append({
        "Sport": sport,
        "Game": game,
        "Type": bet_type,
        "Line": line,
        "Amount": amount,
        "Result": result
    })
    st.success("✅ Bet added successfully.")

if st.session_state.bets:
    st.subheader("📋 Tracked Bets")
    df = pd.DataFrame(st.session_state.bets)
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    st.session_state.bets = edited_df.to_dict("records")

    stats = edited_df.groupby("Type").agg({
        "Amount": "sum"
    }).rename(columns={"Amount": "Total Wagered"})

    st.subheader("📊 Stats by Bet Type")
    st.dataframe(stats)
else:
    st.info("No bets tracked yet.")