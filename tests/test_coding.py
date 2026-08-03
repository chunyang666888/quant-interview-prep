from qip import coding as C


def test_median():
    assert C.median([3, 1, 2]) == 2
    assert C.median([1, 2, 3, 4]) == 2.5


def test_percentile():
    xs = list(range(1, 101))
    assert C.percentile(xs, 0) == 1.0
    assert C.percentile(xs, 100) == 100.0
    assert C.percentile(xs, 50) == 50.5


def test_is_prime():
    assert not C.is_prime(0)
    assert not C.is_prime(1)
    assert C.is_prime(2) and C.is_prime(3)
    assert not C.is_prime(4)
    assert C.is_prime(97)


def test_fib():
    assert C.fib(0) == 0
    assert C.fib(1) == 1
    assert C.fib(10) == 55


def test_most_frequent():
    assert C.most_frequent([1, 2, 2, 3, 3, 3]) == (3, 3)


def test_shuffle_length_preserved():
    xs = list(range(20))
    out = C.shuffle(xs)
    assert sorted(out) == xs


def test_memo_fib():
    f = C.memo_fib()
    assert f(20) == 6765
    assert f(50) == 12586269025
