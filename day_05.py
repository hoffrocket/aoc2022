from collections import deque

import aoc

input = aoc.get_input(5, False)

example = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def stack_game(game: str, deque_append_func) -> str:
    stack_str, inst_str = game.split("\n\n")
    stacks = []
    for row in stack_str.splitlines()[:-1]:
        for column, value in enumerate(row[1::4]):
            if len(stacks) < column + 1:
                stacks.append(deque())
            if value.strip():
                stacks[column].append(value)

    for inst in inst_str.splitlines():
        _, count, _, origin, _, dest = inst.strip().split(" ")
        stage = deque()
        for _ in range(0, int(count)):
            value = stacks[int(origin) - 1].popleft()
            deque_append_func(stage, value)
        stacks[int(dest) - 1].extendleft(stage)

    return "".join(stack[0] for stack in stacks)


def part1(game: str) -> str:
    return stack_game(game, deque.append)


def part2(game: str) -> str:
    return stack_game(game, deque.appendleft)


assert part1(example) == "CMZ"
print(part1(input))


assert part2(example) == "MCD"
print(part2(input))
