"""Solved probability & expectation problems common in quant/trading interviews.

Every function is a small, self-contained, well-known result — the kind of
question that shows up on a whiteboard. Implemented from first principles so
the *reasoning* is visible, not just the answer.
"""

from functools import lru_cache


def expected_flips_for_pattern(pattern: str) -> float:
    """Expected fair-coin flips until ``pattern`` first appears (e.g. ``'HH'``).

    Uses Conway's leading-overlap algorithm: a pattern of length *n* needs on
    average ``2**n`` flips, plus ``2**(n-i)`` for every proper prefix that is
    also a suffix of length *i*.
    """
    pattern = pattern.upper()
    n = len(pattern)
    if n == 0:
        return 0.0
    expected = 2.0 ** n
    for i in range(1, n):
        if pattern[:i] == pattern[n - i:]:
            expected += 2.0 ** (n - i)
    return expected


def expected_rolls_for_six() -> float:
    """Expected fair-die rolls until the first 6.

    Geometric with p = 1/6  ->  E = 1/p = 6.
    """
    return 6.0


def monty_hall(switch: bool) -> float:
    """Win probability in the Monty Hall problem.

    ``switch=True`` wins with probability 2/3 (the host's reveal is informative).
    """
    return 2 / 3 if switch else 1 / 3


def random_walk_ruin(p: float, a: int, b: int) -> float:
    """P(hit ``+a`` before ``-b``) for a biased random walk.

    Starts at 0; each step +1 w.p. ``p``, -1 w.p. ``1-p``; absorbing at
    ``+a`` and ``-b`` (a, b > 0).
    """
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive integers")
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be in [0, 1]")
    if p == 0.5:
        return a / (a + b)
    q = 1.0 - p
    r = q / p
    return (1.0 - r ** b) / (1.0 - r ** (a + b))


def expected_max_of_n_uniform(n: int) -> float:
    """E[max(U1, …, Un)] for Ui ~ Uniform(0, 1).

    The max has CDF x**n, so its expectation is n/(n+1).
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    return n / (n + 1)


def birthday_probability(people: int, days: int = 365) -> float:
    """Probability that at least two of ``people`` share a birthday."""
    if people < 2:
        return 0.0
    if people > days:
        return 1.0
    distinct = 1.0
    for i in range(people):
        distinct *= (days - i) / days
    return 1.0 - distinct


def expected_draws_until_duplicate(days: int = 365) -> float:
    """Expected draws (with replacement) until the first repeated value.

    For the classic 365-day birthday setting the answer is ≈ 24.62.
    """
    prob_distinct = 1.0
    expected = 0.0
    for k in range(2, days + 2):
        p_repeat_at_k = prob_distinct * ((k - 1) / days)
        expected += k * p_repeat_at_k
        prob_distinct *= (days - (k - 1)) / days
    return expected
