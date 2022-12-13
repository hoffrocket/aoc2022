import functools
import operator
from collections import deque
from typing import Callable, Dict, List, NamedTuple, Tuple

import aoc

input = aoc.get_input(12)

example = """Sabqponm
             abcryxxl
             accszExk
             acctuvwj
             abdefghi""".splitlines()


def part1(rows: List[str]) -> int:
    grid = list(map(list, map(str.strip, rows)))

    def find_letter(l):
        return next(
            (
                x,
                y,
            )
            for y, row in enumerate(grid)
            for x, value in enumerate(row)
            if value == l
        )

    start_x, start_y = find_letter("S")
    end_x, end_y = find_letter("E")
    grid[end_y][end_x] = "z"
    distances = {
        (
            start_x,
            start_y,
        ): 0
    }
    queue = deque()
    queue.append(
        (
            start_x,
            start_y,
        )
    )
    visited = set()
    while queue:
        x, y = queue.popleft()
        visited.add(
            (
                x,
                y,
            )
        )
        current_char = grid[y][x]
        current_value = ord(current_char)
        if current_char == "S":
            current_value = 999
        candidates = [
            (
                ix,
                iy,
            )
            for ix, iy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if (ix in range(0, len(grid[0])) and iy in range(0, len(grid)) and ord(grid[iy][ix]) - current_value <= 1)
        ]
        # print(x, y, candidates)
        for tup in candidates:
            distances[tup] = (
                distances[
                    (
                        x,
                        y,
                    )
                ]
                + 1
            )
            if tup not in visited and tup not in queue:
                queue.append(tup)

    # print(distances)
    return distances[
        (
            end_x,
            end_y,
        )
    ]


assert part1(example) == 31, part1(example)
print(part1(input))
