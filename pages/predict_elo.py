import streamlit as st
from predictive_models.model_manager import ModelManager

st.title("📈 Elo Predictions")

model_mgr = ModelManager()
historical_games = [
    {'team_a': 'Cowboys', 'team_b': 'Texans', 'winner': 'Cowboys'},
    {'team_a': 'Texans', 'team_b': 'Chiefs', 'winner': 'Chiefs'},
]
model_mgr.train_from_history(historical_games)

team_a = st.text_input("Enter Team A", "Cowboys")
team_b = st.text_input("Enter Team B", "Texans")

if st.button("Predict Matchup"):
    prediction = model_mgr.predict_game(team_a, team_b)
    st.write("Prediction:", prediction)