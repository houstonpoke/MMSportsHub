from predictive_models.elo import EloModel

class ModelManager:
    def __init__(self):
        self.elo_model = EloModel()

    def train_from_history(self, historical_games):
        for game in historical_games:
            team_a = game['team_a']
            team_b = game['team_b']
            result = 1 if game['winner'] == team_a else 0
            self.elo_model.update_ratings(team_a, team_b, result)

    def predict_game(self, team_a, team_b):
        prob = self.elo_model.predict(team_a, team_b)
        return {
            'team_a_win_prob': round(prob, 3),
            'team_b_win_prob': round(1 - prob, 3),
            'elo_diff': self.elo_model.get_rating(team_a) - self.elo_model.get_rating(team_b)
        }