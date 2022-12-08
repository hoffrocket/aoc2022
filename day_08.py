from typing import Dict, List, NamedTuple, Tuple

import aoc

input = aoc.get_input(8)


example = """30373
25512
65332
33549
35390""".splitlines()


def part1(rows: List[str]) -> int:
    grid = [list(map(int, l.strip())) for l in rows]
    height = len(grid)
    width = len(grid[0])
    vis_count = 0
    for y in range(0, height):
        for x in range(0, width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                vis_count += 1
            else:
                current_tree = grid[y][x]
                is_visible = (
                    max(grid[y][0:x]) < current_tree
                    or max(grid[y][x + 1 : width]) < current_tree
                    or max(grid[i][x] for i in range(0, y)) < current_tree
                    or max(grid[i][x] for i in range(y + 1, height)) < current_tree
                )
                if is_visible:
                    vis_count += 1

    return vis_count


assert part1(example) == 21, part1(example)
print(part1(input))


def part2(rows: List[str]) -> int:
    def count_eaves(current_tree: int, l: List[int]):
        count = 0
        for i in l:
            if i >= current_tree:
                return count + 1
            else:
                count += 1
        return count

    grid = [list(map(int, l.strip())) for l in rows]
    height = len(grid)
    width = len(grid[0])
    max_vis_score = 0
    for y in range(0, height):
        for x in range(0, width):
            current_tree = grid[y][x]
            vis_score = (
                count_eaves(current_tree, reversed(grid[y][0:x]))
                * count_eaves(current_tree, grid[y][x + 1 : width])
                * count_eaves(current_tree, reversed([grid[i][x] for i in range(0, y)]))
                * count_eaves(current_tree, [grid[i][x] for i in range(y + 1, height)])
            )
            max_vis_score = max(max_vis_score, vis_score)

    return max_vis_score


assert part2(example) == 8, part2(example)
print(part2(input))
