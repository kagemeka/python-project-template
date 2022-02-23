"""Mypy Inline Configs.
see https://mypy.readthedocs.io/en/stable/inline_config.html
# mypy: disallow-untyped-defs = False
# mypy:
"""


def add(lhs: int, rhs: int) -> int:
    """Add two integers.

    Args:
        lhs (int): an integer.
        rhs (int): an integer.

    Returns:
        int: sum of lhs and rhs.
    """
    return lhs + rhs
