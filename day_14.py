import functools
import itertools
import operator
from typing import List

import aoc

input = aoc.get_input(14)

example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()


def part1(lines: List[str]) -> int:
    source = tuple([500, 0])
    paths = [[tuple(map(int, point_str.split(","))) for point_str in line.strip().split(" -> ")] for line in lines]
    # print(paths)
    rocks = set()
    for path in paths:
        assert len(path) > 1
        for i in range(0, len(path) - 1):
            src, dest = path[i], path[i + 1]
            for y in range(min(src[1], dest[1]), max(src[1], dest[1]) + 1):
                rocks.add(tuple([src[0], y]))
            for x in range(min(src[0], dest[0]), max(src[0], dest[0]) + 1):
                rocks.add(tuple([x, src[1]]))
    # print(rocks)
    sands = set()
    all_items = set(rocks)

    def get_rest_point(x, y):
        ys = [p[1] for p in all_items if p[0] == x and p[1] > y]
        if ys:
            return (x, min(ys) - 1)
        return None

    sx, sy = source

    loop_count = 100_000_000
    while loop_count:
        loop_count -= 1
        rest_point = get_rest_point(sx, sy)
        if not rest_point:
            break
        else:
            # print("rest point", rest_point)
            sx, sy = rest_point
            if (sx - 1, sy + 1) not in all_items:
                sx = sx - 1
                sy = sy + 1
            elif (sx + 1, sy + 1) not in all_items:
                sx = sx + 1
                sy = sy + 1
            else:
                # print("adding", sx, sy)
                sands.add((sx, sy))
                all_items.add((sx, sy))
                sx, sy = source
    # print(sands)
    return len(sands)


aoc.assert_equals(24, part1(example))
print(part1(input))


# def part2(lines:  List[str]) -> int:
#     return 0


# aoc.assert_equals(140, part2(example))
# print(part2(input))
