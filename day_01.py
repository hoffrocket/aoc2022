import os
from collections import namedtuple

input = open("day_01.txt").read()


cal_max = 0
all_cals = []
for elf_meals in input.split("\n\n"):
    cal_sum = sum(map(int, elf_meals.split("\n")))
    all_cals.append(cal_sum)
    cal_max = max(cal_sum, cal_max)

# part 1
print(cal_max)

# part 2
all_cals.sort(reverse=True)
top_3 = all_cals[:3]
print(top_3)
print(sum(top_3))
