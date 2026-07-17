from app.calculations.poisson import poisson_probability, calculate_over_25


def test_poisson_probability():
    result = poisson_probability(2.0, 2)

    assert result > 0


def test_over_25():
    result = calculate_over_25(3.0)

    assert result > 0
    assert result <= 100