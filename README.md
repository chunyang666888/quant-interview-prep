# quant-interview-prep

Solved **quant & trading interview problems** in Python — the kind that shows up on a whiteboard.
Three self-contained, dependency-free modules; every function implements the result *from first
principles* so the reasoning is visible, not just the answer.

[![CI](https://github.com/chunyang666888/quant-interview-prep/actions/workflows/ci.yml/badge.svg)](https://github.com/chunyang666888/quant-interview-prep/actions)

```
pip install -e .
pytest -q
```

## What's inside

| Module | Coverage |
|--------|----------|
| `qip.probability`   | fair-coin pattern expectation (Conway), Monty Hall, random-walk ruin, birthday paradox, expected max of uniforms |
| `qip.brainteasers`  | ants on a stick, 100 doors, Fermi estimate (ping-pong balls in 747), balance-scale odd-coin, two-trains-and-a-fly |
| `qip.coding`        | median / percentile (no numpy), primality, Fibonacci (+ memoized closure), mode, Fisher-Yates shuffle |

## Examples

```python
from qip import probability as P, brainteasers as B, coding as C

P.expected_flips_for_pattern("HH")          # 6.0
P.birthday_probability(23)                  # 0.5073
B.hundred_doors(100)                        # 10
B.two_train_fly(100, 50, 50, 100)          # 100.0
C.percentile(list(range(1, 101)), 50)      # 50.5
C.is_prime(97)                             # True
```

Run the tour: `python examples/interview_demo.py`

## Why this repo

Interviewers at quant / trading desks love first-principles probability, brainteasers, and
"build-it-from-scratch" coding. This repo is my working notebook for exactly those — each
function is small, tested, and explains itself.

## License

MIT
