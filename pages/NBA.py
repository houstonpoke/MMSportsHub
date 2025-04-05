import streamlit as st
st.title("🏀 NBA - MM Sports Hub")

st.markdown("### Live Odds & Model Prediction")
st.write("Odds: Team A -110, Team B +105")
st.write("Elo Prediction: Team A win prob = 58%")
st.write("Logistic Model: Team A = 61%")
st.write("Expected Value: +4.5%")
st.write("📊 Morrow's Edge: 5.3 🟢 High Confidence")

st.markdown("### Track Your Bet")
st.text_input("Team")
st.selectbox("Bet Type", ["Moneyline", "Spread", "Over/Under"])
st.number_input("Odds", value=-110)
st.number_input("Wager ($)", value=10)
st.button("Add Bet")