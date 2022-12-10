from typing import Dict, List, NamedTuple, Tuple

import aoc

input = aoc.get_input(10)


example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()


def part1(rows: List[str]) -> int:
    cycles = [20, 60, 100, 140, 180, 220]
    clock = 0
    x = 1
    signal_strength = 0
    for row in rows:
        parts = row.strip().split(" ")
        op = parts[0]
        inc = 1 if op == "noop" else 2
        inst_signal = next((c for c in cycles if c == clock + 1 or c == clock + inc), None)
        if inst_signal:
            # print("recording at ", inst_signal, clock, inc, x)
            signal_strength += inst_signal * x
        clock += inc
        if op == "addx":
            x += int(parts[1])
    return signal_strength


assert part1(example) == 13140, part1(example)
print(part1(input))


def part2(rows: List[str]) -> str:
    pixels = [list(x) for x in ([list("." * 40)] * 6)]
    row_index = 0
    clock = 0
    x = 1
    for row in rows:
        parts = row.strip().split(" ")
        op = parts[0]
        inc = 1 if op == "noop" else 2
        for _ in range(0, inc):
            if clock in [x - 1, x, x + 1]:
                pixels[row_index][clock] = "#"
            clock += 1
            if clock == 40:
                clock = 0
                row_index += 1
        if op == "addx":
            x += int(parts[1])

    return "\n".join("".join(row) for row in pixels)


assert (
    part2(example)
    == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
), part2(example)
print(part2(input))
