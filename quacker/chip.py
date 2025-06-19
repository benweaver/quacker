from dataclasses import dataclass

@dataclass(frozen=True)
class Chip:
    """Single chip drawn from a bag.

    Attributes
    ----------
    color: str
        The color of the chip, e.g. 'orange' or 'white'.
    value: int
        The numeric value printed on the chip.
    """
    color: str
    value: int
