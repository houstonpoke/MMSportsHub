import streamlit as st
from data_integrations.odds_api import get_real_odds

st.title("🏀 NCAA Basketball - MM Sports Hub")

st.markdown("### Live Odds & Analysis (Stub - Full Logic Next)")
odds = get_real_odds(sport="basketball_ncaab", market="h2h,spreads,totals")
if isinstance(odds, list):
    for game in odds[:3]:
        st.subheader(f"{game['away_team']} @ {game['home_team']}")
        st.write("Odds data and analysis loading...")
else:
    st.error("Failed to load odds.")