from __future__ import annotations

import random
from typing import Dict, Iterable, List

from .chip import Chip


class Bag:
    """A collection of ingredient chips that can be drawn at random."""

    def __init__(self, contents: Dict[str, Iterable[int]]):
        self._chips: List[Chip] = []
        for color, values in contents.items():
            for value in values:
                self._chips.append(Chip(color=color, value=value))

    def draw(self) -> Chip:
        """Remove and return a random chip from the bag."""
        if not self._chips:
            raise ValueError("Cannot draw from an empty bag")
        index = random.randrange(len(self._chips))
        return self._chips.pop(index)

    def __len__(self) -> int:
        return len(self._chips)

    def contents(self) -> List[Chip]:
        """Return a copy of the current bag contents."""
        return list(self._chips)
