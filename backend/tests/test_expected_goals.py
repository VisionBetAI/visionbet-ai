from app.calculations.expected_goals import (
    calculate_expected_goals,
    calculate_match_xg
)


def test_expected_goals():
    result = calculate_expected_goals(
        1.5,
        1.0,
        1.4
    )

    assert result > 0


def test_match_xg():
    result = calculate_match_xg(
        1.5,
        1.0,
        1.2,
        1.1,
        1.4
    )

    assert "home_expected_goals" in result
    assert "away_expected_goals" in result

    assert result["home_expected_goals"] > 0
    assert result["away_expected_goals"] > 0