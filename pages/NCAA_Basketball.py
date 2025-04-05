import streamlit as st
from data_integrations.odds_api import get_real_odds

st.title("🏀 NCAA Basketball - MM Sports Hub")

st.markdown("### Live Odds & Model Prediction")
odds = get_real_odds(sport="basketball_ncaab")
if isinstance(odds, list):
    for game in odds[:3]:
        st.subheader(f"{game['away_team']} @ {game['home_team']}")
        if game.get('bookmakers'):
            book = game['bookmakers'][0]
            st.write(f"Bookmaker: {book['title']}")
            for outcome in book['markets'][0]['outcomes']:
                st.write(f"{outcome['name']}: {outcome['price']}")
else:
    st.error("Failed to load odds.")

st.markdown("### Track Your Bet")
st.text_input("Team")
st.selectbox("Bet Type", ["Moneyline", "Spread", "Over/Under"])
st.number_input("Odds", value=-110)
st.number_input("Wager ($)", value=10)
st.button("Add Bet")