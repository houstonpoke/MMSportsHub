import streamlit as st
from data_integrations.odds_api import get_mock_odds
from predictive_models.model_manager import ModelManager

st.set_page_config(page_title="MM Sports Hub", layout="wide")
st.title("🤠 MM Sports Hub")

st.subheader("Top Game of the Day")

odds = get_mock_odds()
st.markdown(f"**{odds['game']}**")
st.write("Odds:", odds['odds'])

model_mgr = ModelManager()
model_mgr.train_from_history([
    {'team_a': 'Cowboys', 'team_b': 'Texans', 'winner': 'Cowboys'},
    {'team_a': 'Texans', 'team_b': 'Chiefs', 'winner': 'Chiefs'},
])
result = model_mgr.predict_game("Cowboys", "Texans")

st.write("Model Prediction:", result)
st.markdown("---")

# ✅ FIXED MULTILINE MARKDOWN BLOCK
st.markdown("""
### Navigate to pages:
- 📈 [Elo Predictions](pages/predict_elo.py)
- 🔬 [Research Hub](pages/research_hub.py)
""")
