import streamlit as st
from data_integrations.odds_api import get_real_odds
from predictive_models.model_manager import ModelManager

st.set_page_config(page_title="MM Sports Hub", layout="wide")
st.title("🤠 MM Sports Hub")
st.markdown("## 📊 Today's Top Games (Live Odds + Model Predictions)")

# --- Get Real Odds ---
odds_data = get_real_odds(sport="basketball_nba")

# --- Initialize Elo Model ---
model_mgr = ModelManager()
model_mgr.train_from_history([
    {'team_a': 'Lakers', 'team_b': 'Warriors', 'winner': 'Lakers'},
    {'team_a': 'Warriors', 'team_b': 'Clippers', 'winner': 'Clippers'},
])

# --- Show Top Games ---
if isinstance(odds_data, list) and len(odds_data) > 0:
    for game in odds_data[:5]:  # Show top 5 games
        home = game['home_team']
        away = game['away_team']
        teams = f"{away} @ {home}"

        # Model Prediction
        prediction = model_mgr.predict_game(away, home)
        team_a_win = prediction['team_a_win_prob']
        team_b_win = prediction['team_b_win_prob']
        edge = abs(team_a_win - 0.5)

        # Confidence Color
        if edge > 0.15:
            confidence = "🟢 High"
        elif edge > 0.08:
            confidence = "🟡 Medium"
        else:
            confidence = "🔴 Low"

        st.subheader(teams)
        st.write(f"📈 Model Prediction: {away} {int(team_a_win*100)}% | {home} {int(team_b_win*100)}%")
        st.write(f"📊 Confidence Level: {confidence}")

        if game.get('bookmakers'):
            book = game['bookmakers'][0]
            st.write(f"🧾 Bookmaker: {book['title']}")
            for outcome in book['markets'][0]['outcomes']:
                st.write(f"{outcome['name']}: {outcome['price']}")
        st.markdown("---")
else:
    st.error("Failed to load live odds. Check your API key or request limit.")

# --- Navigation Help ---
st.markdown("""
### 🔀 Navigation:
- 📈 Use sidebar or pages folder to open `Elo Predictions`
- 🔬 Open `Research Hub` for glossary and stats
""")
