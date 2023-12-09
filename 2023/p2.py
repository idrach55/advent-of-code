import sys
from typing import Dict, List, Tuple

import regex


def parse(line: str) -> Tuple[int, List[Dict[str, int]]]:
    game_id = int(line.split(":")[0].split(" ")[1])
    results = line.split(":")[1].split(";")
    sets = []
    for result in results:
        draw = {}
        for batch in regex.findall("[0-9]+ [a-z]+", result):
            val, color = batch.split(" ")
            draw[color] = int(val)
        sets.append(draw)
    return game_id, sets


def part2(lines: List[str]) -> int:
    powers = []
    for l in lines:
        game_id, sets = parse(l)
        mins = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for result in sets:
            for color in mins.keys():
                mins[color] = max(mins[color], result.get(color, 0))
        p = mins["red"] * mins["green"] * mins["blue"]
        powers.append(p)
    return sum(powers)


def part1(lines: List[str]) -> int:
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    valid_games = []
    for l in lines:
        game_id, sets = parse(l)
        valid = True
        for result in sets:
            for color in cubes.keys():
                valid &= result.get(color, 0) <= cubes[color]
        if valid:
            valid_games.append(game_id)
    return sum(valid_games)


if __name__ == "__main__":
    assert len(sys.argv) == 2
    text = open(sys.argv[1]).read()
    lines = [l for l in text.split("\n") if len(l) > 0]
    print(part2(lines))
