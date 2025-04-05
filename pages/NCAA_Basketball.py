import streamlit as st
st.title("🏀 NCAA Basketball - MM Sports Hub")

st.markdown("### Live Odds & Model Prediction")
st.write("Odds: Team A -125, Team B +115")
st.write("Elo Prediction: Team A win prob = 54%")
st.write("Logistic Model: Team A = 57%")
st.write("Expected Value: +3.2%")
st.write("📊 Morrow's Edge: 4.1 🟡 Medium Confidence")

st.markdown("### Track Your Bet")
st.text_input("Team")
st.selectbox("Bet Type", ["Moneyline", "Spread", "Over/Under"])
st.number_input("Odds", value=-110)
st.number_input("Wager ($)", value=10)
st.button("Add Bet")