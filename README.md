# Quacker

Quacker is a simulation tool for exploring different strategies in the board game **The Quacks of Quedlinburg**. The tool repeatedly draws tokens from a bag according to the game's rules and measures how many victory points and rubies the player would earn.

The simulator expects two main pieces of information:

1. **Bag of tokens** – the starting contents of the player's bag. This includes the white chips and any ingredient chips from the selected ingredient set.
2. **Strategy functions** – small bits of logic that decide when to stop drawing and how to handle any choices that come up during the game (such as when to spend rubies).

The simulator runs thousands of trial games and reports the average and variance of the points and rubies earned. This lets you compare different strategies or ingredient sets.

## Installation

Quacker requires Python 3.8 or newer.

```bash
pip install -r requirements.txt  # Not yet provided
```

(At the moment there is no packaged release; clone this repository and run the scripts directly.)

## Usage

There is not yet a command line interface, but a typical simulation session looks like the following in Python:

```python
from quacker.sim import run_simulation
from quacker.strategies import stop_at_7

bag = {
    "white": [1, 1, 1, 2, 2, 3],
    "pumpkin": [1, 1, 1],
    # add other ingredient chips here
}

result = run_simulation(
    bag=bag,
    ingredient_set="Set 1",  # corresponds to entries in data/ingredients.json
    stop_when=stop_at_7,
    iterations=10000,
)

print(result)
```

The `data/ingredients.json` file lists the different ingredient sets available in the game and the effects of each chip. Each entry describes how the chip interacts with the pot when it is drawn.

## Contributing

This repository is under early development. Bug reports and pull requests are welcome. The TODO list includes

- Creating a solid command line interface
- Adding strategy functions for more complex decisions
- Integrating the scoring rules for various fortune teller cards

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more information.
