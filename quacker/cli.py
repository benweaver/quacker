import argparse
import re

from . import Bag, StopAt, stop_before_big_white, StopAtChance, simulate_round


def parse_bag(bag_desc: str) -> Bag:
    """Parse a bag description string into a Bag.

    The description should be a comma separated list like
    "orange1,green1,white1x4" where the optional ``xN`` suffix
    specifies that chip repeated ``N`` times.
    """
    contents = {}
    for item in bag_desc.split(','):
        item = item.strip()
        if not item:
            continue
        count = 1
        if 'x' in item:
            token, count_part = item.split('x', 1)
            item = token.strip()
            count = int(count_part)
        match = re.match(r"([a-zA-Z]+)(\d+)", item)
        if not match:
            raise ValueError(f"Invalid chip descriptor: {item}")
        color, value = match.groups()
        value = int(value)
        contents.setdefault(color, []).extend([value] * count)
    return Bag(contents)


STRATEGIES = {
    'stop_at': StopAt,
    'stop_before_big_white': stop_before_big_white,
    'stop_at_chance': StopAtChance,
}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Quacker simulation CLI")
    parser.add_argument('--bag', required=True,
                        help='Bag composition e.g. "orange1,white1x4"')
    parser.add_argument('--strategy', choices=list(STRATEGIES.keys()),
                        default='stop_before_big_white',
                        help='Strategy to use')
    parser.add_argument('--threshold', type=int,
                        help='Threshold for stop_at or stop_before_big_white')
    parser.add_argument('--chance', type=float,
                        help='Probability for stop_at_chance')
    args = parser.parse_args(argv)

    bag = parse_bag(args.bag)

    if args.strategy == 'stop_at':
        threshold = args.threshold if args.threshold is not None else 7
        strategy = StopAt(threshold)
    elif args.strategy == 'stop_before_big_white':
        threshold = args.threshold if args.threshold is not None else 7
        strategy = stop_before_big_white(threshold)
    elif args.strategy == 'stop_at_chance':
        probability = args.chance if args.chance is not None else 0.5
        strategy = StopAtChance(probability)
    else:
        raise ValueError('Unknown strategy')

    cauldron, exploded = simulate_round(bag, strategy)
    print("Drawn:", [(c.color, c.value) for c in cauldron.chips()])
    print("Total white:", cauldron.white_total())
    print("Exploded:", exploded)


if __name__ == '__main__':
    main()
