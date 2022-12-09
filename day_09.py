from typing import Dict, List, NamedTuple, Tuple

import aoc

input = aoc.get_input(9)


example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()


def part1(rows: List[str]) -> int:
    t_x, t_y, h_x, h_y = 0, 0, 0, 0
    t_positions = set()
    # fmt: off
    t_positions.add((0, 0,))
    # fmt: off
    dir_map = dict(R=(1, 0,), L=(-1, 0,), U=(0,1,), D=(0,-1,))
    for row in rows:
        dir, quant_s = row.strip().split(" ")
        quant = int(quant_s)
        d_x, d_y = dir_map[dir]
        # print("moving H by ", dir, quant, d_x, d_y)
        for _ in range(0, quant):
            h_x += d_x
            h_y += d_y
            dt_x = h_x - t_x
            dt_y = h_y - t_y
            if abs(dt_x) == 2:
                t_x += dt_x//2
                t_y += dt_y
                # print("new t pos", t_x, t_y, "h_pos", h_x, h_y)
            elif abs(dt_y) == 2:
                t_y += dt_y//2
                t_x += dt_x
                # print("new t pos", t_x, t_y, "h_pos", h_x, h_y)

            t_positions.add((t_x, t_y, ))

    # print(t_positions)
    return len(t_positions)


assert part1(example) == 13, part1(example)
print(part1(input))


def part2(rows: List[str], t_count: int = 9) -> int:
    h_x, h_y = 0, 0
    knots = list(range(1, t_count + 1))
    pos_map = {
        knot: (
            0,
            0,
        )
        for knot in knots
    }
    assert len(pos_map) == t_count
    t_positions = set()
    # fmt: off
    t_positions.add((0, 0,))
    # fmt: off
    dir_map = dict(R=(1, 0,), L=(-1, 0,), U=(0,1,), D=(0,-1,))
    for row in rows:
        dir, quant_s = row.strip().split(" ")
        quant = int(quant_s)
        d_x, d_y = dir_map[dir]
        # print("moving H by ", dir, quant, d_x, d_y)
        for _ in range(0, quant):
            h_x += d_x
            h_y += d_y
            rh_x, rh_y = h_x, h_y
            for knot in knots:
                t_x, t_y = pos_map[knot]
                dt_x = rh_x - t_x
                dt_y = rh_y - t_y
                if abs(dt_x) > 1:
                    t_x += dt_x//abs(dt_x)
                    if dt_y != 0:
                        t_y += dt_y//abs(dt_y)
                elif abs(dt_y) > 1:
                    t_y += dt_y//abs(dt_y)
                    if dt_x != 0:
                        t_x += dt_x//abs(dt_x)
                if knot == t_count:
                    t_positions.add((t_x, t_y, ))
                pos_map[knot] = (t_x, t_y,)
                rh_x, rh_y = t_x, t_y

    # print(t_positions)
    return len(t_positions)


assert part2(example, 1) == 13, part2(example, 1)
assert part2(example) == 1, part2(example)
example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines()
assert part2(example2) == 36, part2(example2)
print(part2(input))
