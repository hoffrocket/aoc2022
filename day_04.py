from typing import List

import aoc

lines = aoc.get_input(4)

example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()


def range_checker(lines: List[str], func) -> int:
    count = 0
    for pair_str in lines:
        parts = pair_str.strip().split(",")
        range1, range2 = [range(*map(int, p.split("-"))) for p in parts]
        if func(range1, range2):
            count += 1
    return count


def part1(lines: List[str]) -> int:
    def range_contains(x, y):
        """is x fully in y"""
        return x.start >= y.start and x.stop <= y.stop

    return range_checker(lines, lambda r1, r2: range_contains(r1, r2) or range_contains(r2, r1))


def part2(lines: List[str]) -> int:
    def range_overlap(r1, r2):
        return (r1.start >= r2.start and r1.start <= r2.stop) or (r1.stop <= r2.stop and r1.stop >= r2.start)

    return range_checker(lines, lambda r1, r2: range_overlap(r1, r2) or range_overlap(r2, r1))


assert part1(example) == 2
print(part1(lines))


assert part2(example) == 4
print(part2(lines))
