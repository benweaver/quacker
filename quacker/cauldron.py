from __future__ import annotations

from typing import Iterable, List, Optional

from .chip import Chip


class Cauldron:
    """Container for chips that have been drawn in the current round."""

    def __init__(self, chips: Iterable[Chip] | None = None):
        self._chips: List[Chip] = list(chips) if chips else []

    def add(self, chip: Chip) -> None:
        """Add a chip to the cauldron."""
        self._chips.append(chip)

    def last_chip(self) -> Optional[Chip]:
        """Return the most recently added chip or ``None``."""
        return self._chips[-1] if self._chips else None

    def __len__(self) -> int:
        return len(self._chips)

    def total_value(self) -> int:
        """Sum of all chip values currently in the cauldron."""
        return sum(c.value for c in self._chips)

    def white_total(self) -> int:
        """Sum of white chip values currently in the cauldron."""
        return sum(c.value for c in self._chips if c.color == "white")

    def chips(self) -> List[Chip]:
        """Return a copy of chips currently in the cauldron."""
        return list(self._chips)
