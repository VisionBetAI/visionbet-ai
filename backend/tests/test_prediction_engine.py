from app.engine.prediction_engine import PredictionEngine


def test_prediction_engine():

    engine = PredictionEngine()

    result = engine.analyze_match(
        home_team="Palmeiras",
        away_team="Flamengo",
        home_attack=1.45,
        home_defense=0.92,
        away_attack=1.30,
        away_defense=1.05,
        league_average_goals=1.35
    )

    assert result["home_team"] == "Palmeiras"
    assert result["away_team"] == "Flamengo"

    assert "expected_goals" in result
    assert "top_scores" in result

    assert len(result["top_scores"]) == 10