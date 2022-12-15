import functools
import itertools
import operator
import re
from collections import defaultdict
from typing import List, NamedTuple, Tuple

import aoc

input = aoc.get_input(15)

example = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()


def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def merge_ranges(ranges: List[range]) -> List[range]:
    """https://stackoverflow.com/questions/43600878/merging-overlapping-intervals"""
    if not ranges:
        return ranges
    sorted_ranges = sorted(ranges, key=lambda r: r.start)
    merged = [sorted_ranges[0]]
    for current in sorted_ranges:
        previous = merged[-1]
        if current.start <= previous.stop:
            merged[-1] = range(previous.start, max(previous.stop, current.stop))
        else:
            merged.append(current)
    return merged


class Sensor(NamedTuple):
    sx: int
    sy: int
    bx: int
    by: int
    dist: int

    def row_in_range(self, y) -> bool:
        return self.dist_to_row(y) <= self.dist

    def dist_to_row(self, y) -> int:
        return abs(self.sy - y)

    def free_ranges_for_row(self, y) -> List[Tuple[int, int]]:
        dist_y = self.dist_to_row(y)
        dist_x = max(self.dist - dist_y, 0)
        if dist_x > 0:
            xr = range(self.sx - dist_x, self.sx + dist_x + 1)
            if self.by == y and self.bx in xr:
                return [range(xr.start, self.bx), range(self.bx + 1, xr.stop)]
            else:
                return [xr]
        else:
            return []

    @classmethod
    def from_points(cls, sx, sy, bx, by) -> "Sensor":
        return Sensor(sx, sy, bx, by, man_dist(sx, sy, bx, by))


def ranges_for_row(sensors: List[Sensor], row: int) -> List[range]:
    x_ranges = [rs for s in sensors for rs in s.free_ranges_for_row(row) if s.row_in_range(row)]
    return merge_ranges(x_ranges)


def part1(lines: List[str], row: int) -> int:
    sensors = [Sensor.from_points(*map(int, re.findall("-?\d+", line.strip()))) for line in lines]
    # print(f"{sensors=}")
    merged_ranges = ranges_for_row(sensors, row)
    # print(f"{merged_ranges=}")
    return sum(r.stop - r.start for r in merged_ranges)


aoc.assert_equals(26, part1(example, 10))
print(part1(input, 2000000))


def part2(lines: List[str], pmax: int) -> int:
    sensors = [Sensor.from_points(*map(int, re.findall("-?\d+", line.strip()))) for line in lines]
    # print(f"{sensors=}")
    beacon_coords = set((s.bx, s.by) for s in sensors)
    max_row = min(pmax, max(s.sy for s in sensors))
    for row in range(0, max_row + 1):
        covered_ranges = ranges_for_row(sensors, row)
        if len(covered_ranges) > 1:
            print(f"{row=},{covered_ranges=}")
            for next_range in covered_ranges[1:]:
                gap_x = next_range.start - 1
                if gap_x in range(0, pmax + 1) and (gap_x, row) not in beacon_coords:
                    print(f"Found: {gap_x=},{row=}")
                    return gap_x * pmax + row


aoc.assert_equals(56000011, part2(example, 4000000))
print(part2(input, 4000000))
