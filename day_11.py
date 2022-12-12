import functools
import operator
from typing import Callable, Dict, List, NamedTuple, Tuple

import aoc

input = aoc.get_input(11)

example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()


class Monkey:
    def __init__(self, id: int):
        self.id = id
        self.operation: str = None
        self.operand: str = None
        self.test: int = 0
        self.true_action: str = None
        self.false_action: str = None
        self.items: List[int] = None

    def operate(self, old: int):
        op = operator.add if self.operation == "+" else operator.mul
        return op(old, old) if self.operand == "old" else op(int(self.operand), old)

    def __repr__(self):
        return f"Monkey[{self.id},{self.items}, {self.test},{self.true_action},{self.false_action},{self.operation},{self.operand}]"


def solution(rows: List[str], worry_discount: int, num_rounds: int) -> int:
    current_monkey = None
    monkeys = []
    for row in rows:
        tokens = row.strip().split(" ")
        if tokens[0] == "Monkey":
            current_monkey = Monkey(int(tokens[1][:-1]))
            monkeys.append(current_monkey)
        if tokens[0] == "Starting":
            current_monkey.items = [int(m.replace(",", "")) for m in tokens[2:]]
        elif tokens[0] == "Operation:":
            current_monkey.operation = tokens[4]
            current_monkey.operand = tokens[5]
        elif tokens[0] == "Test:":
            current_monkey.test = int(tokens[3])
        elif tokens[0] == "If":
            if tokens[1] == "true:":
                current_monkey.true_action = int(tokens[5])
            elif tokens[1] == "false:":
                current_monkey.false_action = int(tokens[5])
    # print("Start", monkeys)

    inspection_counts = [0] * len(monkeys)
    test_product = functools.reduce(operator.mul, [m.test for m in monkeys])
    for round in range(1, num_rounds + 1):
        for monkey in monkeys:
            for item in monkey.items:
                inspection_counts[monkey.id] += 1
                new_item = monkey.operate(item) // worry_discount
                next_monkey = monkeys[monkey.true_action if new_item % monkey.test == 0 else monkey.false_action]
                if worry_discount == 1:
                    next_monkey.items.append(new_item % test_product)
                else:
                    next_monkey.items.append(new_item)
            monkey.items = []
        # print(f"Round {round}", monkeys)
    # print("inspection_counts", inspection_counts)
    return functools.reduce(operator.mul, sorted(inspection_counts, reverse=True)[:2])


def part1(rows: List[str]) -> int:
    return solution(rows, 3, 20)


assert part1(example) == 10605, part1(example)
print(part1(input))


def part2(rows: List[str]) -> int:
    return solution(rows, 1, 10000)


assert part2(example) == 2713310158
print(part2(input))
