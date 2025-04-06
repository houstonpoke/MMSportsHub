ELO_RATINGS = {
    "Lakers": 1600,
    "Celtics": 1650,
    "Florida": 1655,
    "Auburn": 1640,
    "Duke": 1685,
    "Houston": 1700,
    "Alabama": 1620,
    "UConn": 1750
}

TEAM_ALIASES = {
    "Los Angeles Lakers": "Lakers",
    "Boston Celtics": "Celtics",
    "Florida Gators": "Florida",
    "Auburn Tigers": "Auburn",
    "Duke Blue Devils": "Duke",
    "Houston Cougars": "Houston",
    "Alabama Crimson Tide": "Alabama",
    "Connecticut Huskies": "UConn"
}

def get_elo(team):
    key = TEAM_ALIASES.get(team, team)
    return ELO_RATINGS.get(key, 1500)

def win_probability(team_a, team_b):
    rating_a = get_elo(team_a)
    rating_b = get_elo(team_b)

    # Elo-based expected probability
    elo_prob = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    # Simulated logistic regression layer
    logistic_prob = 1 / (1 + 10 ** ((rating_b - rating_a) / 300))

    # Combined model prediction
    final_prob = round((elo_prob + logistic_prob) / 2, 3)

    return final_prob, rating_a, rating_b