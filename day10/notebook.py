# https://adventofcode.com/2020/day/10
#%%

with open("sample1.txt") as f:
    numbers = [int(n) for n in f.read().split("\n")]

#%%

with open("sample2.txt") as f:
    numbers = [int(n) for n in f.read().split("\n")]

#%%

with open("input.txt") as f:
    numbers = [int(n) for n in f.read().split("\n")]

#%%


def part_one(numbers):
    # We need to start from 0
    numbers = sorted(numbers + [0])

    one_diff = 0
    three_diff = 0

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if diff > 3:
            break
        if diff == 3:
            three_diff += 1
        if diff == 1:
            one_diff += 1

    # builtin difference
    three_diff += 1

    return one_diff * three_diff


part_one(numbers)

# %%
from functools import cache  # Python 3.9


def part_two(numbers):
    # We need to start from 0
    numbers = sorted(numbers + [0])

    @cache
    def possible_paths(index):
        paths = 0

        for i in range(index + 1, len(numbers)):
            if numbers[i] - numbers[index] > 3:
                break

            paths += possible_paths(i)

        if paths == 0:
            # if no possible paths, we arrived to the end
            return 1

        return paths

    return possible_paths(0)


part_two(numbers)
# %%
