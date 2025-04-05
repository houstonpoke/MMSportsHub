import streamlit as st
st.title("⛳ Golf - MM Sports Hub")

st.markdown("### Outright Odds & Model Prediction")
st.write("Player: John Smith")
st.write("Odds: +2200")
st.write("Form Score: 88")
st.write("Strokes Gained Total: +1.4")
st.write("📊 Morrow's Edge: 6.2 🟢 High Confidence")

st.markdown("### Track Your Bet")
st.text_input("Player")
st.selectbox("Bet Type", ["To Win", "Top 10", "Top 20"])
st.number_input("Odds", value=2200)
st.number_input("Wager ($)", value=10)
st.button("Add Bet")