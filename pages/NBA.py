import streamlit as st
from sportsbook_api import get_sportsbook_odds
from edge_legend import show_edge_legend
import time

show_edge_legend()

st.title("🏀 NBA - Live Odds (Sportsbook API)")

if "nba_odds_cache" not in st.session_state:
    st.session_state.nba_odds_cache = None
    st.session_state.nba_last_refresh = 0

st.markdown("Click to fetch the latest NBA odds from Sportsbook API.")
if st.button("🔄 Refresh Odds"):
    st.session_state.nba_odds_cache = get_sportsbook_odds(league="NBA")
    st.session_state.nba_last_refresh = time.time()

# Limit pulls: only refresh if manually triggered
odds_data = st.session_state.nba_odds_cache
last_updated = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.session_state.nba_last_refresh))

if odds_data and isinstance(odds_data, dict) and "advantages" in odds_data:
    st.success(f"✅ Odds last updated: {last_updated}")
    for match in odds_data["advantages"][:10]:  # Show top 10 matchups
        game = match.get("game", {})
        home = game.get("homeTeam", {}).get("name", "Home")
        away = game.get("awayTeam", {}).get("name", "Away")
        st.subheader(f"{away} @ {home}")

        for book in match.get("bookmakers", []):
            st.markdown(f"**{book.get('title', 'Bookmaker')}**")
            for market in book.get("markets", []):
                st.markdown(f"- {market.get('type')}: {market.get('outcome')} @ {market.get('price')}")
        st.markdown("---")
else:
    st.warning("⚠️ No odds available. Please click 'Refresh Odds' to pull data.")