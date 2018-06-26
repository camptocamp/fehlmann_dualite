import argparse
import requests
from typing import List


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--nb', type=int, default=1000000)

    return parser.parse_args()


def _get_bit(byte: int, pos: int) -> str:
    return '1' if byte & (1 << pos) else '0'


def main() -> None:
    args = _parse_args()
    random: List[int] = []
    for pos in range(0, args.nb, 2):
        if len(random) == 0:
            nb = min(10000, (args.nb - pos) / 2)
            r = requests.get(f'https://www.random.org/integers/?num={nb}&' +
                             'min=0&max=63&col=1&base=10&format=plain&rnd=new')
            random = [int(v) for v in r.text.split("\n") if v != '']
        byte = random.pop()
        out = ",".join(_get_bit(byte, pos) for pos in range(0, 3))
        print(out)
        if pos + 1 < args.nb:
            out = ",".join(_get_bit(byte, pos) for pos in range(3, 6))
            print(out)


if __name__ == "__main__":
    main()
