from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Tuple

from .bag import Bag
from .cauldron import Cauldron

# Type alias for a stop strategy function
StopStrategy = Callable[[Bag, Cauldron], bool]

EXPLOSION_THRESHOLD = 7


def simulate_round(bag: Bag, strategy: StopStrategy) -> Tuple[Cauldron, bool]:
    """Simulate drawing chips for a single round.

    Parameters
    ----------
    bag:
        The ``Bag`` to draw chips from. It will be modified by this function.
    strategy:
        A callable deciding whether to stop drawing. It is invoked after each
        draw with the current state.

    Returns
    -------
    cauldron: ``Cauldron`` containing all drawn chips.
    exploded: ``bool`` indicating whether the cauldron exploded.
    """
    cauldron = Cauldron()
    exploded = False

    while len(bag) > 0:
        chip = bag.draw()
        cauldron.add(chip)
        if chip.color == "white" and cauldron.white_total() > EXPLOSION_THRESHOLD:
            exploded = True
            break
        if strategy(bag, cauldron):
            break

    return cauldron, exploded


@dataclass
class StopAt:
    """Stop once the total value of white chips reaches ``threshold``."""

    threshold: int = EXPLOSION_THRESHOLD

    def __call__(self, bag: Bag, cauldron: Cauldron) -> bool:
        return cauldron.white_total() >= self.threshold


def stop_before_big_white(threshold: int = EXPLOSION_THRESHOLD) -> StopStrategy:
    """Return a strategy that stops if any remaining white chip would explode."""

    def strategy(bag: Bag, cauldron: Cauldron) -> bool:
        current = cauldron.white_total()
        for chip in bag.contents():
            if chip.color == "white" and current + chip.value > threshold:
                return True
        return False

    return strategy


def explosion_chance(bag: Bag, cauldron: Cauldron, threshold: int = EXPLOSION_THRESHOLD) -> float:
    """Probability that the next draw will cause an explosion."""
    if len(bag) == 0:
        return 0.0
    current = cauldron.white_total()
    risky = 0
    for chip in bag.contents():
        if chip.color == "white" and current + chip.value > threshold:
            risky += 1
    return risky / len(bag)


@dataclass
class StopAtChance:
    """Stop once the explosion chance exceeds ``probability``."""

    probability: float

    def __call__(self, bag: Bag, cauldron: Cauldron) -> bool:
        return explosion_chance(bag, cauldron) > self.probability

