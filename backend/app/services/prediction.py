from app.calculations.expected_goals import calculate_match_xg


def generate_prediction(
    home_team: str,
    away_team: str,
    home_attack: float,
    home_defense: float,
    away_attack: float,
    away_defense: float,
    league_average_goals: float
) -> dict:
    """
    Generates a match prediction.
    """

    xg = calculate_match_xg(
        home_attack,
        home_defense,
        away_attack,
        away_defense,
        league_average_goals
    )

    return {
        "home_team": home_team,
        "away_team": away_team,
        "expected_goals": xg
    }