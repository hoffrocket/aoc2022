from typing import Dict, List, NamedTuple, Tuple

import aoc

input = aoc.get_input(7)


class Dir(NamedTuple):
    name: str
    parent_dir: "Dir"
    files: List[Tuple[int, str]]
    dirs: List["Dir"]


example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()


def get_size_totals(console: List[str]) -> Dict[str, int]:
    root_dir = Dir("/", None, [], [])
    current_dir = root_dir
    for line in console[1:]:
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                dir_name = parts[2].strip()
                if dir_name == "..":
                    new_dir = current_dir.parent_dir
                else:
                    new_dir = next(dir for dir in current_dir.dirs if dir.name == dir_name)
                current_dir = new_dir
        else:
            if parts[0] == "dir":
                current_dir.dirs.append(Dir(parts[1].strip(), current_dir, [], []))
            else:
                current_dir.files.append(
                    (
                        int(parts[0]),
                        parts[1],
                    )
                )

    def calc_size(dir: Dir, totals):
        file_sum = sum(f[0] for f in dir.files)
        dir_total = file_sum
        for d in dir.dirs:
            dir_total += calc_size(d, totals)
        totals[dir.name] = dir_total
        return dir_total

    totals = {}
    calc_size(root_dir, totals)
    return totals


def part1(console: List[str]) -> int:
    totals = get_size_totals(console)
    return sum(t for t in totals.values() if t <= 100000)


assert part1(example) == 95437
print(part1(input))


def part2(console: List[str]) -> int:
    totals = get_size_totals(console)
    total_space = 70000000
    free_space_target = 30000000
    space_used = totals["/"]
    current_free_space = total_space - space_used
    space_needed = free_space_target - current_free_space
    winner = (
        "",
        999999999999,
    )
    for d, d_space in totals.items():
        if d_space >= space_needed and d_space <= winner[1]:
            winner = (
                d,
                d_space,
            )
    return winner[1]


assert part2(example) == 24933642
print(part2(input))
