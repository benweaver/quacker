# Quacker

`Quacker` is a simulation and analysis tool for the board game **The Quacks of Quedlinburg**. It is designed to evaluate different in-game strategies by repeatedly simulating draws from a player's bag of ingredient chips.

The simulator accepts the composition of a bag and one or more strategy functions. A *stop strategy* determines whether to continue drawing chips or to stop for the current round. Additional strategy functions can modify behaviour such as chip purchasing or optional effects. By running thousands of simulations the tool reports the average and variance of points and rubies gained.

The ingredient data used by the simulator is stored in [`data/ingredients.json`](data/ingredients.json). Each ingredient set lists chip colours, costs and the rules text for their bonuses.

## Repository Contents

- **`data/ingredients.json`** – JSON file describing all known ingredient sets.
- **`quacker/` code (forthcoming)** – the Python package implementing the simulator.

## Simulation Outline

1. **Setup** – Construct a bag of ingredient chips and choose the ingredient set.
2. **Stop Strategy** – Provide a function that receives the current state (bag contents, drawn chips and running total) and returns `True` to stop or `False` to draw again.
3. **Optional Strategies** – Additional hooks can be used to implement buying decisions, token upgrades and other game logic.
4. **Execution** – The simulator draws chips from the bag until the stop strategy halts the round or the bag explodes. This is repeated for many runs.
5. **Results** – Average victory points and rubies are returned along with variance, allowing comparison of strategies.

## Example Usage

```python
from quacker import simulate_game, StopAt

bag = {
    'white': [1, 1, 2, 3],  # chip values
    'orange': [1, 1],
    'blue': [1],
}

# stop drawing once 7 white points are showing
stop = StopAt(threshold=7)

stats = simulate_game(bag, stop, runs=10000)
print(stats)
```

Example output might look like:

```
Average points: 8.3 ± 2.4
Average rubies: 1.1 ± 0.6
```

## Future Work

The repository currently focuses on the ingredient data and simulation design. Future versions will include:

- A full command line interface for running experiments.
- Additional strategy helpers and pre-made stop conditions.
- Visualisations for bag composition and results.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for more information.

