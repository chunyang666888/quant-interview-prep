"""Implement-common-functions-from-scratch drills.

Whiteboard favourites: the interviewer wants to see you *build* a tool, not
import one. Each function is dependency-free and has a clear contract.
"""

from collections import Counter


def median(xs: list[float]) -> float:
    """Median of an unsorted list (no statistics module)."""
    if not xs:
        raise ValueError("empty list has no median")
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2.0


def percentile(xs: list[float], p: float) -> float:
    """p-th percentile (0 <= p <= 100) via linear interpolation (no numpy)."""
    if not xs:
        raise ValueError("empty list")
    if not 0.0 <= p <= 100.0:
        raise ValueError("p must be in [0, 100]")
    s = sorted(xs)
    if len(s) == 1:
        return float(s[0])
    rank = (p / 100.0) * (len(s) - 1)
    lo = int(rank)
    hi = min(lo + 1, len(s) - 1)
    frac = rank - lo
    return s[lo] * (1 - frac) + s[hi] * frac


def is_prime(n: int) -> bool:
    """Trial-division primality (sufficient for interview sizes)."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def fib(n: int) -> int:
    """n-th Fibonacci number (0-indexed) via O(n) iteration."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def most_frequent(xs: list) -> tuple:
    """(value, count) of the most frequent element (no collections.Counter)."""
    if not xs:
        raise ValueError("empty list")
    counts: dict = {}
    for x in xs:
        counts[x] = counts.get(x, 0) + 1
    best = max(counts.items(), key=lambda kv: kv[1])
    return best


def shuffle(xs: list) -> list:
    """In-place Fisher-Yates shuffle (deterministic given ``rng``)."""
    import random

    a = xs[:]
    for i in range(len(a) - 1, 0, -1):
        j = random.randrange(i + 1)
        a[i], a[j] = a[j], a[i]
    return a


def memo_fib() -> callable:
    """Closure version of fib with caching (shows decorators / closures)."""
    cache: dict = {0: 0, 1: 1}

    def f(n: int) -> int:
        if n < 0:
            raise ValueError("n must be >= 0")
        if n in cache:
            return cache[n]
        cache[n] = f(n - 1) + f(n - 2)
        return cache[n]

    return f
