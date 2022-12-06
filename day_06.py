import aoc

input = aoc.get_input(6, False)


example = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


def part1(buffer: str) -> int:
    for i in range(0, len(buffer)):
        sub = buffer[i : i + 4]
        if len(set(sub)) == 4:
            return i + 4


assert part1(example) == 7
print(part1(input))


def part2(buffer: str) -> int:
    for i in range(0, len(buffer)):
        sub = buffer[i : i + 14]
        if len(set(sub)) == 14:
            return i + 14


assert part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
print(part2(input))
