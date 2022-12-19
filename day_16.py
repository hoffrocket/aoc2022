import functools
import itertools
import operator
import re
from collections import defaultdict
from typing import List, NamedTuple, Tuple
from collections import deque
import copy

import aoc

input = aoc.get_input(16)

example = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()


class Valve(NamedTuple):
    id: str
    rate: int
    next: List[id]

def part1(lines: List[str]) -> int:
    valves = [
        Valve(valve[0], int(valve[1]), valve[2].split(", "))
        for line in lines
        for valve in re.findall("Valve\s(..)\s.+=(\d+);.+valves?\s(.+)", line.strip())
    ]
    print(valves)
    aoc.assert_equals(len(lines), len(valves))
    queue = deque()
    queue.append((valves[0],1, {}, defaultdict(set)))
    valve_map = {
        v[0]:v for v in valves
    }
    max_score = 0
    # best_plan = None
    while queue:
        valve, minute, is_on, path_map = queue.pop()
        if minute == 30:
            current_score = sum(v[0] for v in is_on.values())
            if current_score > max_score:
                print("new minute 30 high score:", current_score, is_on)
                max_score = current_score
        else:
            next_valves = [
                valve_map[vid]
                for vid in valve.next
                if vid not in path_map[valve.id] or (
                    vid not in is_on
                    or
                    valve_map[vid].rate == 0
                )
            ]
            for v in next_valves:
                path_map_copy = copy.deepcopy(path_map)
                path_map_copy[valve.id].add(v.id)
                # print(minute, "exploring next valve",v.id, valve, is_on, path_map)
                queue.append((v, minute + 1, is_on, path_map_copy))

            if valve.rate > 0 and not valve.id in is_on:
                is_on_copy = is_on.copy()
                remaining_minutes = (30 - minute)
                rate_score =  remaining_minutes * valve.rate
                is_on_copy[valve.id] = (rate_score, minute, remaining_minutes)
                # print(minute, "turning on valve score",rate_score, valve, is_on, path_map)
                queue.append((valve, minute + 1, is_on_copy, path_map))

            if not next_valves:
                # print(minute, "no where to go from ", valve, is_on, path_map)
                queue.append((valve, minute + 1, is_on, path_map))

    return max_score


aoc.assert_equals(1651, part1(example))
print(part1(input))
