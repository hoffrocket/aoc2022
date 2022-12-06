import aoc

input = aoc.get_input(6, False)


example = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


def solve(buffer: str, ctl_len: int) -> int:
    return next(i + ctl_len for i in range(0, len(buffer)) if len(set(buffer[i : i + ctl_len])) == ctl_len)


def part1(buffer: str) -> int:
    return solve(buffer, 4)


assert part1(example) == 7
print(part1(input))


def part2(buffer: str) -> int:
    return solve(buffer, 14)


assert part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
print(part2(input))
