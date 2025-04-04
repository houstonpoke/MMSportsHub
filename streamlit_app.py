import streamlit as st
from data_integrations.odds_api import get_mock_odds
from predictive_models.model_manager import ModelManager

st.set_page_config(page_title="MM Sports Hub", layout="wide")
st.title("🤠 MM Sports Hub")
st.subheader("Today's Top Game")

# Load mock odds
odds = get_mock_odds()
st.markdown(f"### {odds['game']}")
st.write("Moneyline Odds:")
st.write(f"🏈 {list(odds['odds'].keys())[0]}: {odds['odds'][list(odds['odds'].keys())[0]]}")
st.write(f"🏈 {list(odds['odds'].keys())[1]}: {odds['odds'][list(odds['odds'].keys())[1]]}")

# Predict game outcome using Elo
model_mgr = ModelManager()
model_mgr.train_from_history([
    {'team_a': 'Cowboys', 'team_b': 'Texans', 'winner': 'Cowboys'},
    {'team_a': 'Texans', 'team_b': 'Chiefs', 'winner': 'Chiefs'},
])
result = model_mgr.predict_game("Cowboys", "Texans")

st.write("📊 Model Prediction:", result)
st.markdown("---")
st.markdown("""
### Navigation:
- 📈 Go to `pages/predict_elo.py` for Elo Predictions
- 🔬 Go to `pages/research_hub.py` for Model Research
""")