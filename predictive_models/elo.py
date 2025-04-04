class EloModel:
    def __init__(self, base_rating=1500, k_factor=20):
        self.ratings = {}
        self.base_rating = base_rating
        self.k = k_factor

    def get_rating(self, team):
        return self.ratings.get(team, self.base_rating)

    def expected_score(self, team_a, team_b):
        ra = self.get_rating(team_a)
        rb = self.get_rating(team_b)
        return 1 / (1 + 10 ** ((rb - ra) / 400))

    def update_ratings(self, team_a, team_b, result):
        expected_a = self.expected_score(team_a, team_b)
        expected_b = 1 - expected_a
        self.ratings[team_a] = self.get_rating(team_a) + self.k * (result - expected_a)
        self.ratings[team_b] = self.get_rating(team_b) + self.k * ((1 - result) - expected_b)

    def predict(self, team_a, team_b):
        return self.expected_score(team_a, team_b)