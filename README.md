# Quacker

Quacker is a simulation tool for exploring strategies in **The Quacks of Quedlinburg**. It allows you to evaluate different approaches by repeatedly simulating draws from a bag of ingredient tokens.

The simulator accepts:

- An initial bag composition (number and type of tokens)
- A **stop-when** strategy function that decides when to stop drawing based on the current pot and bag state
- Additional strategy helpers as desired (for example, when to use flasks, when to buy particular ingredients, etc.)

Running the simulator many times provides statistics on the average victory points and rubies earned as well as their variance. This helps compare the long‑term performance of various strategies.

Ingredient set information can be found in [`data/ingredients.json`](data/ingredients.json). Each set describes how the colored chips behave at different chip values. You can extend or modify this file to reflect expansions or house rules.

## Usage

The main entry point will be a Python module (coming soon) that loads your bag configuration and strategy functions, runs thousands of simulated games, and prints a summary of the results. A typical workflow looks like:

1. Define your bag of starting tokens.
2. Implement a `stop_when(pot_state, bag_state)` strategy function.
3. Run the simulator specifying the number of iterations.
4. Inspect the reported averages and adjust your strategy as desired.

Detailed examples and API documentation will be added once the simulation engine is in place.

## Project Structure

```
README.md            - Project overview (this file)
LICENSE              - MIT license
src/                 - Simulation engine (planned)
data/ingredients.json - Definitions of ingredient sets
```

## Contributing

Pull requests are welcome! Feel free to open an issue to discuss improvements or share strategy ideas.

## License

This project is licensed under the [MIT License](LICENSE).
