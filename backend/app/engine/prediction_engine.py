from app.calculations.expected_goals import calculate_match_xg
from app.calculations.score_prediction import generate_score_probabilities


class PredictionEngine:
    """
    Central engine responsible for orchestrating match analysis.
    """

    def analyze_match(
        self,
        home_team: str,
        away_team: str,
        home_attack: float,
        home_defense: float,
        away_attack: float,
        away_defense: float,
        league_average_goals: float,
    ) -> dict:

        expected_goals = calculate_match_xg(
            home_attack,
            home_defense,
            away_attack,
            away_defense,
            league_average_goals,
        )

        scores = generate_score_probabilities(
            expected_goals["home_expected_goals"],
            expected_goals["away_expected_goals"],
        )

        return {
            "home_team": home_team,
            "away_team": away_team,
            "expected_goals": expected_goals,
            "top_scores": scores[:10],
        }