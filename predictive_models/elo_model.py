ELO_RATINGS = {
    "Lakers": 1600,
    "Celtics": 1650,
    "Duke": 1500,
    "Kansas": 1525,
    "Gonzaga": 1510
}

def get_elo(team):
    return ELO_RATINGS.get(team, 1500)

def win_probability(team_a, team_b):
    rating_a = get_elo(team_a)
    rating_b = get_elo(team_b)
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    return round(expected_a, 2)