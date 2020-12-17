#%%
import numpy as np


def parse_file(filename):
    with open(filename) as f:
        lines = f.read().split("\n")

    space = np.zeros((len(lines[0]), len(lines), 1))

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                space[y][x][0] = 1

    return space


def make_new_cell_function(space):
    def get_new_cell(*indices):
        # translate to old space
        indices = [i - 1 for i in indices]

        matrix = space[tuple(slice(max(i - 1, 0), i + 2) for i in indices)]

        if all(0 <= i < dim for i, dim in zip(indices, space.shape)):
            previous_value = space[tuple(indices)]
        else:
            previous_value = 0

        active_neighbors = matrix.sum() - previous_value

        if previous_value:
            return int(active_neighbors in [2, 3])

        return int(active_neighbors == 3)

    return get_new_cell


def part_one(space):
    for _ in range(6):
        space = np.fromfunction(
            np.vectorize(make_new_cell_function(space)),
            [i + 2 for i in space.shape],
            dtype=int,
        )

    return space.sum()


# assert part_one(parse_file("sample.txt")) == 112

part_one(parse_file("input.txt"))

# %%

## PART TWO
def parse_file_2(filename):
    with open(filename) as f:
        lines = f.read().split("\n")

    space = np.zeros((len(lines[0]), len(lines), 1, 1))

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                space[y][x][0][0] = 1

    return space


# assert part_one(parse_file_2("sample.txt")) == 848

part_one(parse_file_2("input.txt"))
