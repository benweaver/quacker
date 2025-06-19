from __future__ import annotations

from typing import List, Tuple

from .cauldron import Cauldron

# Progress thresholds for awarding victory points. Each tuple contains the
# exclusive upper bound for progress and the points granted when progress is
# below that bound.
VP_TABLE: List[Tuple[int, int]] = [
    (6, 0),
    (10, 1),
    (14, 2),
    (18, 3),
    (22, 4),
    (26, 5),
    (29, 6),
    (32, 7),
    (35, 8),
    (38, 9),
    (41, 10),
    (44, 11),
    (48, 12),
    (51, 13),
    (53, 14),
    (float('inf'), 15),
]

# Progress spaces that award a ruby.
RUBY_SPACES = {5, 9, 13, 16, 20, 24, 28, 30, 34, 36, 40, 42, 46, 50, 52}

def progress(cauldron: Cauldron) -> int:
    """Return the total value of all chips in ``cauldron``."""
    return cauldron.total_value()

def victory_points(p: int) -> int:
    """Return the victory points for the given progress value."""
    for threshold, vp in VP_TABLE:
        if p < threshold:
            return vp
    # Fallback shouldn't be reached but return the final VP value
    return VP_TABLE[-1][1]

def rubies(p: int) -> int:
    """Return the number of rubies for the given progress value."""
    return 1 if p in RUBY_SPACES else 0

def score_cauldron(cauldron: Cauldron) -> Tuple[int, int]:
    """Calculate victory points and rubies earned from ``cauldron``."""
    p = progress(cauldron)
    return victory_points(p), rubies(p)
