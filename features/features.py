def build_features(game_stats):
    # Placeholder for building features from game stats
    return [
        game_stats.get("team_a_score", 0) - game_stats.get("team_b_score", 0),
        game_stats.get("team_a_yards", 0),
        game_stats.get("team_b_yards", 0),
    ]