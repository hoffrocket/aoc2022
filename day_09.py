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
                t_x += d_x
                t_y += dt_y
                # print("new t pos", t_x, t_y, "h_pos", h_x, h_y)
            elif abs(dt_y) == 2:
                t_y += d_y
                t_x += dt_x
                # print("new t pos", t_x, t_y, "h_pos", h_x, h_y)

            t_positions.add((t_x, t_y, ))

    # print(t_positions)
    return len(t_positions)


assert part1(example) == 13, part1(example)
print(part1(input))
