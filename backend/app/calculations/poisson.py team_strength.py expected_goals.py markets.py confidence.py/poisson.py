import math


def poisson_probability(lamb: float, goals: int) -> float:
    """
    Calculates the probability of scoring a specific number of goals.
    """

    return (
        (math.exp(-lamb) * (lamb ** goals))
        / math.factorial(goals)
    )


def calculate_over_25(lamb: float) -> float:
    """
    Calculates probability of over 2.5 goals.
    """

    probability = 0

    for goals in range(3, 10):
        probability += poisson_probability(lamb, goals)

    return round(probability * 100, 2)