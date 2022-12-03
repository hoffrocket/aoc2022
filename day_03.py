from functools import reduce
from typing import List

import aoc

lines = aoc.get_input(3)

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()


def get_priorities_part1(rucksack: List[str]):
    total = 0
    for r in rucksack:
        r_len = int(len(r) / 2)

        part1 = set(r[:r_len])
        part2 = set(r[r_len:])
        inter_set = list(part1.intersection(part2))
        assert len(inter_set) == 1
        inter_char = inter_set[0]
        priority_base = 1 if inter_char.islower() else 27
        offset = ord("a") if inter_char.islower() else ord("A")
        priority = ord(inter_char) - offset + priority_base
        total += priority
    return total


assert get_priorities_part1(example) == 157

print(get_priorities_part1(lines))


def get_badges_part2(rucksack: List[str]):
    total = 0
    for index in range(0, len(rucksack), 3):
        group = rucksack[index : index + 3]
        inter_set = list(reduce(lambda s1, s2: s1.intersection(s2), (set(r.strip()) for r in group)))
        assert len(inter_set) == 1
        inter_char = inter_set[0]
        priority_base = 1 if inter_char.islower() else 27
        offset = ord("a") if inter_char.islower() else ord("A")
        priority = ord(inter_char) - offset + priority_base
        total += priority
    return total


assert get_badges_part2(example) == 70

print(get_badges_part2(lines))
