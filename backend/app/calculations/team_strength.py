def calculate_attack_strength(
    goals_scored: float,
    league_average: float
) -> float:
    """
    Calcula a força ofensiva do time.
    """

    if league_average == 0:
        return 0

    return round(goals_scored / league_average, 2)


def calculate_defense_strength(
    goals_conceded: float,
    league_average: float
) -> float:
    """
    Calcula a força defensiva do time.
    """

    if league_average == 0:
        return 0

    return round(goals_conceded / league_average, 2)


def calculate_team_strength(
    goals_scored: float,
    goals_conceded: float,
    league_average_goals: float
) -> dict:
    """
    Retorna um resumo da força do time.
    """

    return {
        "attack_strength": calculate_attack_strength(
            goals_scored,
            league_average_goals
        ),
        "defense_strength": calculate_defense_strength(
            goals_conceded,
            league_average_goals
        )
    }