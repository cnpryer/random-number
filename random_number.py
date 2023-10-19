import random
from argparse import ArgumentParser


def gen(lower: int, upper: int) -> int:
    return random.randint(lower, upper)

def cli() -> None:
    parser = ArgumentParser()
    parser.add_argument("--lower", type=int)
    parser.add_argument("--upper", type=int)

    args = parser.parse_args()
    num = gen(args.lower, args.upper)
    print(num)
