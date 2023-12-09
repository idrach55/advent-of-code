import sys
from typing import List

int_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse(line: str) -> List[int]:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        else:
            for j in range(i + 1, len(line)):
                if line[j].isdigit():
                    break
                if line[i : j + 1] in int_map:
                    digits.append(int_map[line[i : j + 1]])
                    break
    return digits


def part2(lines: List[str]) -> int:
    ints = []
    for l in lines:
        digits = parse(l)
        ints += [10 * digits[0] + digits[-1]]
    return sum(ints)


def part1(lines: List[str]) -> int:
    ints = []
    for l in lines:
        digits = [int(c) for c in l if c.isdigit()]
        ints += [10 * digits[0] + digits[-1]]
    return sum(ints)


if __name__ == "__main__":
    assert len(sys.argv) == 2
    text = open(sys.argv[1]).read()
    lines = [l for l in text.split("\n") if len(l) > 0]
    print(part2(lines))
