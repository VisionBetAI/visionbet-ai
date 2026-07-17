from app.calculations.poisson import poisson_probability


def generate_score_probabilities(
    home_xg: float,
    away_xg: float,
    max_goals: int = 5
) -> list:
    """
    Gera probabilidades de placares usando Poisson.
    """

    scores = []

    for home_goals in range(max_goals + 1):
        for away_goals in range(max_goals + 1):

            probability = (
                poisson_probability(home_xg, home_goals)
                * poisson_probability(away_xg, away_goals)
                * 100
            )

            scores.append({
                "score": f"{home_goals}-{away_goals}",
                "probability": round(probability, 2)
            })

    scores.sort(
        key=lambda item: item["probability"],
        reverse=True
    )

    return scores