from app.services.prediction import generate_prediction


def test_prediction():

    result = generate_prediction(
        "Palmeiras",
        "Flamengo",
        1.5,
        1.0,
        1.2,
        1.1,
        1.4
    )

    assert result["home_team"] == "Palmeiras"
    assert result["away_team"] == "Flamengo"

    assert "expected_goals" in result