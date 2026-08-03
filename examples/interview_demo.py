"""Run a quick tour of quant-interview-prep solutions."""

from qip import probability as P
from qip import brainteasers as B
from qip import coding as C


def main():
    print("== Probability ==")
    print("E[flips for 'HH']        =", P.expected_flips_for_pattern("HH"))
    print("E[flips for 'HHT']       =", P.expected_flips_for_pattern("HHT"))
    print("P(birthday match, 23)    =", round(P.birthday_probability(23), 4))
    print("E[draws until dup, 365]  =", round(P.expected_draws_until_duplicate(), 2))
    print("Ruin p=0.6, +2/-2        =", round(P.random_walk_ruin(0.6, 2, 2), 4))

    print("\n== Brainteasers ==")
    print("Ants max time (stick=1)  =", B.ants_on_stick(1.0))
    print("Open doors among 100     =", B.hundred_doors(100))
    print("Min weighings for 12     =", B.weighing_odd_coin_min_weighings(12))
    print("Fly distance (100/50/50/100)=", B.two_train_fly(100, 50, 50, 100))

    print("\n== Coding from scratch ==")
    print("median([3,1,2])          =", C.median([3, 1, 2]))
    print("percentile 50 of 1..100  =", C.percentile(list(range(1, 101)), 50))
    print("is_prime(97)             =", C.is_prime(97))
    print("fib(20)                  =", C.fib(20))
    print("most_frequent            =", C.most_frequent([1, 2, 2, 3, 3, 3]))


if __name__ == "__main__":
    main()
