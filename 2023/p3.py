import sys
from typing import Dict, List, Tuple

Point = Tuple[int, int]


def parse(text: List[str]) -> Tuple[Dict[Point, int], Dict[Point, int]]:
    numbers = {}
    symbols = {}

    def insertNumber(xs, y, num):
        for x in xs:
            numbers[(x, y)] = int(num)

    for y, l in enumerate(text):
        num = ""
        xs = []
        for x, c in enumerate(l):
            if c.isdigit():
                num += c
                xs += [x]
            else:
                if num != "":
                    insertNumber(xs, y, num)
                    num = ""
                    xs = []
                if c != ".":
                    symbols[(x, y)] = c
        if num != "":
            insertNumber(xs, y, num)
    return numbers, symbols


def part2(text: List[str]) -> int:
    numbers, symbols = parse(text)
    ratios = []
    for (x, y), symbol in symbols.items():
        if symbol != "*":
            continue
        found = set({})
        for x_shift in (-1, 0, 1):
            for y_shift in (-1, 0, 1):
                num = numbers.get((x + x_shift, y + y_shift))
                if num is not None and num not in found:
                    found.add(num)
        if len(found) == 2:
            a, b = tuple(found)
            ratios.append(a * b)
    return sum(ratios)


def part1(text: List[str]) -> int:
    numbers, symbols = parse(text)
    adjacent = []
    for (x, y), symbol in symbols.items():
        found = set({})
        for x_shift in (-1, 0, 1):
            for y_shift in (-1, 0, 1):
                num = numbers.get((x + x_shift, y + y_shift))
                if num is not None and num not in found:
                    adjacent.append(num)
                    found.add(num)
    return sum(adjacent)


if __name__ == "__main__":
    assert len(sys.argv) == 2
    text = open(sys.argv[1]).read()
    lines = [l for l in text.split("\n") if len(l) > 0]
    print(part2(lines))
