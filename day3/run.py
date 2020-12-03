# https://adventofcode.com/2020/day/3
#%%
with open("sample.txt") as f:
    lines = f.read().split("\n")

#%%
with open("input.txt") as f:
    lines = f.read().split("\n")

# %%
row = 0
column = 0
trees = 0

while row < len(lines):
    if lines[row][column] == "#":
        trees += 1

    column = (column + 3) % len(lines[row])
    row += 1

trees

# %%


def get_trees(right, down):
    row = 0
    column = 0
    trees = 0

    while row < len(lines):
        if lines[row][column] == "#":
            trees += 1

        column = (column + right) % len(lines[row])
        row += down

    return trees


slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

mul = 1

for right, down in slopes:
    mul *= get_trees(right, down)

mul
# %%
