def calculate_expected_goals(
    attack_strength: float,
    opponent_defense_strength: float,
    league_average_goals: float,
    home_advantage: float = 1.10
) -> float:
    """
    Calculates expected goals (xG).
    """

    expected_goals = (
        attack_strength
        * opponent_defense_strength
        * league_average_goals
        * home_advantage
    )

    return round(expected_goals, 2)


def calculate_match_xg(
    home_attack: float,
    home_defense: float,
    away_attack: float,
    away_defense: float,
    league_average_goals: float
) -> dict:
    """
    Calculates expected goals for both teams.
    """

    return {
        "home_expected_goals": calculate_expected_goals(
            home_attack,
            away_defense,
            league_average_goals
        ),
        "away_expected_goals": calculate_expected_goals(
            away_attack,
            home_defense,
            league_average_goals,
            home_advantage=1.0
        )
    }