import math
from qip import brainteasers as B


def test_ants_on_stick():
    assert B.ants_on_stick(1.0) == 1.0
    assert B.ants_on_stick(5.0) == 5.0


def test_hundred_doors():
    assert B.hundred_doors(10) == 3
    assert B.hundred_doors(100) == 10
    assert B.hundred_doors(1) == 1


def test_ping_pong_positive():
    v = B.estimate_ping_pong_in_747()
    assert v > 1_000_000


def test_weighing_odd_coin():
    assert B.weighing_odd_coin_min_weighings(3) == 1
    assert B.weighing_odd_coin_min_weighings(9) == 2
    assert B.weighing_odd_coin_min_weighings(12) == 3


def test_two_train_fly():
    # trains 100 apart at 50 each, fly at 100 -> meet in 1h -> fly 100
    assert B.two_train_fly(100, 50, 50, 100) == 100.0
