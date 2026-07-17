from app.calculations.score_prediction import generate_score_probabilities


def test_generate_score_probabilities():

    result = generate_score_probabilities(
        home_xg=1.6,
        away_xg=1.2
    )

    assert len(result) > 0

    assert result[0]["probability"] >= result[1]["probability"]

    assert "score" in result[0]
    assert "probability" in result[0]