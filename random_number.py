import random
from argparse import ArgumentParser
import sys


def gen(lower: int, upper: int) -> int:
    return random.randint(lower, upper)

def cli() -> None:
    parser = ArgumentParser()
    parser.add_argument("-l", "--lower", type=int)
    parser.add_argument("-u", "--upper", type=int)

    args = parser.parse_args()
    num = gen(args.lower or 0, args.upper or sys.maxsize)
    print(num)
