"""Estimation & logic brainteasers seen in trading-desk / quant interviews.

These are the "how many ping-pong balls fit in a 747" style questions. The
point is *structured reasoning under uncertainty*, so each function returns a
number with the assumptions made explicit.
"""

import math


def ants_on_stick(length: float = 1.0) -> float:
    """Max time for all ants to fall off a stick of ``length`` (unit metres).

    Classic trick: when two ants collide and reverse, it's indistinguishable
    from them passing through each other. So the worst case is just the
    farthest distance any single ant must travel = ``length``.
    """
    return float(length)


def hundred_doors(n: int = 100) -> int:
    """How many of ``n`` doors are open after the toggle routine.

    Door *k* is toggled once per divisor it has; only perfect squares have an
    odd number of divisors, so the open doors are the perfect squares.
    """
    if n < 1:
        return 0
    return int(math.isqrt(n))


def estimate_ping_pong_in_747() -> float:
    """Fermi estimate: number of ping-pong balls in a Boeing 747 cabin.

    Assumptions: cabin volume ~ 800 m^3 = 8e8 cm^3; ball diameter 4 cm ->
    ~33 cm^3 raw but packed at ~0.6 density.
    """
    cabin_volume_cm3 = 800 * 1_000_000
    ball_volume_cm3 = (4.0 / 3.0) * math.pi * 2.0 ** 3
    return cabin_volume_cm3 * 0.6 / ball_volume_cm3


def weighing_odd_coin_min_weighings(n: int) -> int:
    """Minimum weighings on a balance scale to find one odd coin among ``n``.

    Each weighing has 3 outcomes, so k weighings distinguish up to 3**k
    possibilities. Answer = ceil(log3(n)).
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    return math.ceil(math.log(n) / math.log(3))


def two_train_fly(distance: float, v1: float, v2: float, vfly: float) -> float:
    """Total distance a fly travels bouncing between two approaching trains.

    The fly's total flight time equals the trains' meeting time
    distance / (v1 + v2); multiply by the fly's speed.
    """
    if v1 <= 0 or v2 <= 0 or vfly <= 0 or distance <= 0:
        raise ValueError("distances/speeds must be positive")
    meet_time = distance / (v1 + v2)
    return vfly * meet_time
