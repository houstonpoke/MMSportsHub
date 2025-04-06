import streamlit as st
from data_integrations.odds_api import get_real_odds
from edge_legend import show_edge_legend

show_edge_legend()

st.title("🎰 Odds Ticker - Vegas Style Board")

sports = {
    "🏀 NBA": "basketball_nba",
    "🏈 NFL": "americanfootball_nfl",
    "🏀 NCAAB": "basketball_ncaab"
}

selected_sport_label = st.selectbox("Select Sport", list(sports.keys()))
sport = sports[selected_sport_label]

odds_data = get_real_odds(sport=sport, market="h2h,spreads,totals")

def get_rotation_number(index):
    base = 301 if "nfl" in sport else 401 if "nba" in sport else 501
    return base + index * 2, base + index * 2 + 1

if isinstance(odds_data, list):
    st.markdown("### 📺 Vegas Board")
    for idx, game in enumerate(odds_data[:10]):
        rot_a, rot_b = get_rotation_number(idx)
        team_a = game['away_team']
        team_b = game['home_team']

        st.markdown(f"**{rot_a} {team_a} @ {rot_b} {team_b}**")

        if game.get('bookmakers'):
            book = game['bookmakers'][0]
            st.write(f"*Bookmaker: {book['title']}*")
            line_info = {}
            for market in book.get("markets", []):
                key = market['key']
                for outcome in market['outcomes']:
                    line_info.setdefault(outcome['name'], {})[key] = outcome['price']

            st.table(line_info)
        st.markdown("---")
else:
    st.error("⚠️ Failed to load odds. Check API status.")