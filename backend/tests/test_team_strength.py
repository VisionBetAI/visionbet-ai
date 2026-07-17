from app.calculations.team_strength import (
    calculate_attack_strength,
    calculate_defense_strength,
    calculate_team_strength
)


def test_attack_strength():
    result = calculate_attack_strength(2.0, 1.0)

    assert result == 2.0


def test_defense_strength():
    result = calculate_defense_strength(0.5, 1.0)

    assert result == 0.5


def test_team_strength():
    result = calculate_team_strength(
        2.0,
        1.0,
        1.0
    )

    assert result["attack_strength"] == 2.0
    assert result["defense_strength"] == 1.0