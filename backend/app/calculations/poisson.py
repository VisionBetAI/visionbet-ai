import math


def poisson_probability(lamb: float, goals: int) -> float:
    return (
        (math.exp(-lamb) * (lamb ** goals))
        / math.factorial(goals)
    )


def calculate_over_25(lamb: float) -> float:
    probability = 0

    for goals in range(3, 10):
        probability += poisson_probability(lamb, goals)

    return round(probability * 100, 2)