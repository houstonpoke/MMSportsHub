import streamlit as st
from data_integrations.odds_api import get_real_odds

def calculate_implied_probability(odds):
    return round(100 / (abs(odds) + 100), 2) if odds > 0 else round(abs(odds) / (abs(odds) + 100), 2)

def display_market_analysis(market_name, outcomes):
    st.write(f"📈 **{market_name}**")
    for outcome in outcomes:
        name = outcome['name']
        price = outcome['price']
        implied = calculate_implied_probability(price)
        st.write(f"{name}: {price} (Implied Win %: {int(implied * 100)}%)")
    st.markdown("---")

st.title("🏀 NBA - MM Sports Hub")

odds = get_real_odds(sport="basketball_nba", market="h2h,spreads,totals")
if isinstance(odds, list):
    for game in odds[:3]:
        st.subheader(f"{game['away_team']} @ {game['home_team']}")
        if game.get('bookmakers'):
            book = game['bookmakers'][0]
            st.write(f"Bookmaker: {book['title']}")
            for market in book['markets']:
                display_market_analysis(market['key'].upper(), market['outcomes'])
else:
    st.error("Failed to load odds.")

st.markdown("### Track Your Bet")
st.text_input("Team")
st.selectbox("Bet Type", ["Moneyline", "Spread", "Over/Under"])
st.number_input("Odds", value=-110)
st.number_input("Wager ($)", value=10)
st.button("Add Bet")