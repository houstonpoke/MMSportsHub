ELO_RATINGS = {
    "Lakers": 1600,
    "Celtics": 1650,
    "Duke": 1500,
    "Kansas": 1525,
    "Gonzaga": 1510
}

TEAM_ALIASES = {
    "Los Angeles Lakers": "Lakers",
    "Boston Celtics": "Celtics",
    "Duke Blue Devils": "Duke",
    "Kansas Jayhawks": "Kansas",
    "Gonzaga Bulldogs": "Gonzaga"
}

def get_elo(team):
    key = TEAM_ALIASES.get(team, team)
    return ELO_RATINGS.get(key, 1500)

def win_probability(team_a, team_b):
    rating_a = get_elo(team_a)
    rating_b = get_elo(team_b)
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    return round(expected_a, 2), rating_a, rating_b