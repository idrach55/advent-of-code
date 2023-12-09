import sys
from typing import List


def part2(text: List[str]) -> int:
    pass


def part1(text: List[str]) -> int:
    pass


if __name__ == "__main__":
    assert len(sys.argv) == 2
    text = open(sys.argv[1]).read()
    lines = [l for l in text.split("\n") if len(l) > 0]
    print(part1(lines))
