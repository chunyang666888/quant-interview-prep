import math
from qip import probability as P


def test_expected_flips_patterns():
    assert P.expected_flips_for_pattern("H") == 2.0
    assert P.expected_flips_for_pattern("HH") == 6.0
    assert P.expected_flips_for_pattern("HT") == 4.0
    assert P.expected_flips_for_pattern("HHT") == 8.0


def test_expected_rolls_for_six():
    assert P.expected_rolls_for_six() == 6.0


def test_monty_hall():
    assert P.monty_hall(True) == 2 / 3
    assert P.monty_hall(False) == 1 / 3


def test_random_walk_ruin_fair():
    assert P.random_walk_ruin(0.5, 1, 1) == 0.5
    assert P.random_walk_ruin(0.5, 2, 2) == 0.5


def test_random_walk_ruin_biased():
    p = P.random_walk_ruin(0.6, 2, 2)
    assert 0.0 < p < 1.0
    assert abs(p - (1 - (0.4 / 0.6) ** 2) / (1 - (0.4 / 0.6) ** 4)) < 1e-9


def test_expected_max_uniform():
    assert P.expected_max_of_n_uniform(1) == 0.5
    assert P.expected_max_of_n_uniform(2) == 2 / 3


def test_birthday():
    assert P.birthday_probability(1) == 0.0
    assert P.birthday_probability(366) == 1.0
    assert 0.99 < P.birthday_probability(70) < 1.0
    assert 0.5 < P.birthday_probability(23) < 0.51


def test_expected_draws_duplicate():
    v = P.expected_draws_until_duplicate(365)
    assert 24.0 < v < 25.0
