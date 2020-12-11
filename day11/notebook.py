# https://adventofcode.com/2020/day/11
#%%


def get_state_from_file(filename):
    with open(filename) as f:
        return [list(row) for row in f.read().split("\n")]


sample_1 = get_state_from_file("sample1.txt")
sample_2 = get_state_from_file("sample2.txt")
sample_3 = get_state_from_file("sample3.txt")
input_state = get_state_from_file("input.txt")
sample_3_2 = get_state_from_file("sample3_2.txt")  # third state for part 2
sample_4_2 = get_state_from_file("sample4_2.txt")  # fourth state for part 2
sample_5_2 = get_state_from_file("sample5_2.txt")
sample_6_2 = get_state_from_file("sample6_2.txt")
sample_7_2 = get_state_from_file("sample7_2.txt")

# %%
from copy import deepcopy


def get_adjacent_seats(row, column, state):
    for i in range(max(row - 1, 0), min(row + 2, len(state))):
        for j in range(max(column - 1, 0), min(column + 2, len(state[0]))):
            if i == row and j == column:
                continue

            yield state[i][j]


def get_next_state(state):
    new_state = deepcopy(state)

    for i in range(len(state)):
        for j in range(len(state[0])):
            seat = state[i][j]
            adjacents = list(get_adjacent_seats(i, j, state))

            if seat == "L" and "#" not in adjacents:
                new_state[i][j] = "#"

            if seat == "#" and len([s for s in adjacents if s == "#"]) >= 4:
                new_state[i][j] = "L"

    return new_state


assert get_next_state(sample_1) == sample_2
assert get_next_state(sample_2) == sample_3


def find_stable_state(initial_state):
    last_state = None
    state = initial_state

    while last_state != state:
        last_state, state = state, get_next_state(state)

    return state


def count_occupied_seats(state):
    return sum((len([s for s in row if s == "#"]) for row in state))


assert count_occupied_seats(find_stable_state(sample_1)) == 37


count_occupied_seats(find_stable_state(input_state))

# %%
from itertools import product


def get_adjacent_seats_2(row, column, state):
    directions = [-1, 0, 1]

    for row_diff, col_diff in product(directions, repeat=2):
        if row_diff == 0 and col_diff == 0:
            continue

        current_row = row + row_diff
        current_col = column + col_diff

        while 0 <= current_row < len(state) and 0 <= current_col < len(state[0]):

            if state[current_row][current_col] == ".":
                current_row += row_diff
                current_col += col_diff
            else:
                yield state[current_row][current_col]
                break


def get_next_state_2(state):
    new_state = deepcopy(state)

    for i in range(len(state)):
        for j in range(len(state[0])):
            seat = state[i][j]

            if seat == ".":
                continue

            adjacents = list(get_adjacent_seats_2(i, j, state))

            if seat == "L" and "#" not in adjacents:
                new_state[i][j] = "#"

            if seat == "#" and len([s for s in adjacents if s == "#"]) >= 5:
                new_state[i][j] = "L"

    return new_state


assert get_next_state_2(sample_2) == sample_3_2
assert get_next_state_2(sample_3_2) == sample_4_2
assert get_next_state_2(sample_4_2) == sample_5_2
assert get_next_state_2(sample_5_2) == sample_6_2
assert get_next_state_2(sample_6_2) == sample_7_2
assert get_next_state_2(sample_7_2) == sample_7_2
assert count_occupied_seats(sample_7_2) == 26


def find_stable_state_2(initial_state):
    last_state = None
    state = initial_state

    while last_state != state:
        last_state, state = state, get_next_state_2(state)

    return state


assert count_occupied_seats(find_stable_state_2(sample_1)) == 26


count_occupied_seats(find_stable_state_2(input_state))

# %%
