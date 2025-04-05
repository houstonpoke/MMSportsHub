import streamlit as st
from data_integrations.odds_api import get_real_odds

st.title("⛳ Golf - The Masters - MM Sports Hub")

st.markdown("### Outright Odds (Stub - Full Logic Next)")
odds = get_real_odds(sport="golf_masters", market="h2h")
if isinstance(odds, list):
    for game in odds[:3]:
        st.subheader(f"{game['home_team']} vs {game['away_team']}")
        st.write("Golf odds and player-level analysis coming soon...")
else:
    st.error("Failed to load odds.")