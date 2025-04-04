import streamlit as st
from predictive_models.model_manager import ModelManager

st.set_page_config(page_title="MM Sports Hub", layout="wide")
st.title("🤠 MM Sports Hub")

st.subheader("Elo Prediction Engine")

model_mgr = ModelManager()

# Example training data
historical_games = [
    {'team_a': 'Cowboys', 'team_b': 'Texans', 'winner': 'Cowboys'},
    {'team_a': 'Texans', 'team_b': 'Chiefs', 'winner': 'Chiefs'},
]
model_mgr.train_from_history(historical_games)

team_a = st.text_input("Team A", "Cowboys")
team_b = st.text_input("Team B", "Texans")

if st.button("Predict Matchup"):
    result = model_mgr.predict_game(team_a, team_b)
    st.write("Win Probabilities:", result)