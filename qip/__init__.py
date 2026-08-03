"""quant-interview-prep — solved quant & trading interview problems in Python.

Three modules:
- ``probability`` : expectation / probability classics (coin patterns, ruin, birthday…)
- ``brainteasers``: estimation & logic puzzles (ants, bridge, 100 doors…)
- ``coding``      : implement-common-functions-from-scratch drills

Pure standard library — no third-party dependencies.
"""

from . import probability, brainteasers, coding

__all__ = ["probability", "brainteasers", "coding"]
