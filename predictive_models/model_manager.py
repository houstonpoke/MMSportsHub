ELO_RATINGS = {
    "Florida": 1655,
    "Auburn": 1640,
    "Houston": 1700,
    "Duke": 1685
}

TEAM_ALIASES = {
    "Florida Gators": "Florida",
    "Auburn Tigers": "Auburn",
    "Houston Cougars": "Houston",
    "Duke Blue Devils": "Duke"
}

def get_elo(team):
    key = TEAM_ALIASES.get(team, team)
    return ELO_RATINGS.get(key, 1500)

def win_probability(team_a, team_b):
    rating_a = get_elo(team_a)
    rating_b = get_elo(team_b)
    elo_prob = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    logistic_prob = 1 / (1 + 10 ** ((rating_b - rating_a) / 300))  # simulate model adjustment
    final_prob = round((elo_prob + logistic_prob) / 2, 3)
    return final_prob, rating_a, rating_b