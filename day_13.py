import functools
import itertools
import json
import operator
from collections import deque
from typing import Callable, Dict, List, NamedTuple, Tuple

import aoc

input = aoc.get_input(13, False)

example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def listwrap(maybe_list):
    return maybe_list if isinstance(maybe_list, list) else [maybe_list]


def correct_order(left, right, depth=0, true_value=True, false_value=False, same_value=None):
    # print(" " * depth, "- Compare ", left, "and", right, true_value, false_value, same_value)
    for li, ri in itertools.zip_longest(left, right):
        if li is None and ri is not None:
            # print(" " * depth, "   left side ran out. TRUE")
            return true_value
        elif li is not None and ri is None:
            # print(" " * depth, "   right side ran out. FALSE")
            return false_value
        elif isinstance(li, list) or isinstance(ri, list):
            result = correct_order(listwrap(li), listwrap(ri), depth + 1, true_value, false_value, same_value)
            # print(" " * depth, "   inner list correct order? ", result)
            if result != same_value:
                return result
        else:
            # print(" " * depth, " - Compare ", li, "vs", ri)
            if li != ri:
                result = li < ri
                # print(" " * depth, "   correct order? ", result)

                return true_value if result else false_value
    # print(" " * depth, "   inner list end of block default of True")
    return same_value


def part1(data: str) -> int:
    pairs = [tuple(map(json.loads, pair_str.splitlines())) for pair_str in data.strip().split("\n\n")]
    # print(pairs)
    correct_indices = [i for i, (left, right) in enumerate(pairs, 1) if correct_order(left, right)]
    # print(correct_indices)
    return sum(correct_indices)


aoc.assert_equals(13, part1(example))
print(part1(input))


def part2(data: str) -> int:
    packets = [json.loads(line) for line in data.strip().splitlines() if line]
    # dividers
    controls = [[[2]], [[6]]]
    packets.extend(controls)
    # print(packets)
    def comp_func(left, right):
        return correct_order(left, right, true_value=-1, false_value=1, same_value=0)

    sorted_packets = sorted(packets, key=functools.cmp_to_key(comp_func))
    # print("sorted:")
    # print(sorted_packets)
    return functools.reduce(
        operator.mul,
        [
            i
            for i, packet in enumerate(sorted_packets, 1)
            if next((True for c in controls if comp_func(c, packet) == 0), False)
        ],
    )


aoc.assert_equals(140, part2(example))
print(part2(input))
