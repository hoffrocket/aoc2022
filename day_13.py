import functools
import itertools
import json
import operator

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


def compare_packets(left, right) -> int:
    for li, ri in itertools.zip_longest(left, right):
        if li is None and ri is not None:
            return -1
        elif li is not None and ri is None:
            return 1
        elif isinstance(li, list) or isinstance(ri, list):
            result = compare_packets(listwrap(li), listwrap(ri))
            if result != 0:
                return result
        else:
            if li != ri:
                return -1 if li < ri else 1
    return 0


def part1(data: str) -> int:
    pairs = [tuple(map(json.loads, pair_str.splitlines())) for pair_str in data.strip().split("\n\n")]
    # print(pairs)
    correct_indices = [i for i, (left, right) in enumerate(pairs, 1) if compare_packets(left, right) < 0]
    # print(correct_indices)
    return sum(correct_indices)


aoc.assert_equals(13, part1(example))
print(part1(input))


def part2(data: str) -> int:
    packets = [json.loads(line) for line in data.strip().splitlines() if line]
    controls = [[[2]], [[6]]]
    packets.extend(controls)
    # print(packets)
    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare_packets))
    # print("sorted:")
    # print(sorted_packets)
    return functools.reduce(
        operator.mul,
        [
            i
            for i, packet in enumerate(sorted_packets, 1)
            if next((True for c in controls if compare_packets(c, packet) == 0), False)
        ],
    )


aoc.assert_equals(140, part2(example))
print(part2(input))
