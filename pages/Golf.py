import streamlit as st
from data_integrations.odds_api import get_real_odds

st.title("⛳ Golf - MM Sports Hub")

st.markdown("### Outright Odds & Prediction")
odds = get_real_odds(sport="golf_masters")
if isinstance(odds, list):
    for game in odds[:3]:
        st.subheader(f"{game['home_team']} vs {game['away_team']}")
        if game.get('bookmakers'):
            book = game['bookmakers'][0]
            st.write(f"Bookmaker: {book['title']}")
            for outcome in book['markets'][0]['outcomes']:
                st.write(f"{outcome['name']}: {outcome['price']}")
else:
    st.error("Failed to load odds.")

st.markdown("### Track Your Bet")
st.text_input("Player")
st.selectbox("Bet Type", ["To Win", "Top 10", "Top 20"])
st.number_input("Odds", value=2200)
st.number_input("Wager ($)", value=10)
st.button("Add Bet")