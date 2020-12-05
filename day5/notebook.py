# https://adventofcode.com/2020/day/5
#%%


def binary_search(lower_bound_char, chars):
    lower_bound = 0
    upper_bound = 2 ** len(chars)

    for char in chars:
        new_bound = (upper_bound + lower_bound) // 2
        if char == lower_bound_char:
            upper_bound = new_bound
        else:
            lower_bound = new_bound

    return lower_bound


def get_seat(seat_code):
    row_chars = seat_code[:7]
    column_chars = seat_code[7:]

    row = binary_search("F", row_chars)
    column = binary_search("L", column_chars)
    seat_id = row * 8 + column

    return row, column, seat_id


assert get_seat("BFFFBBFRRR") == (70, 7, 567)
assert get_seat("FFFBBBFRRR") == (14, 7, 119)
assert get_seat("BBFFBBFRLL") == (102, 4, 820)

print(get_seat("BFFFBBFRRR"))
print(get_seat("FFFBBBFRRR"))
print(get_seat("BBFFBBFRLL"))


# %%
with open("input.txt") as f:
    seats = [(seat_code, get_seat(seat_code)) for seat_code in f.read().split("\n")]

with open("input.txt") as f:
    maximum = max([get_seat(seat_code)[2] for seat_code in f.read().split("\n")])

maximum
# %%
# PART 2

# build whole plane
occupied_seats = [[False for _ in range(8)] for _ in range(128)]

for seat_code, (row, column, id) in seats:
    occupied_seats[row][column] = True


for index, row in enumerate(occupied_seats):
    if index == 0 or False in occupied_seats[index - 1]:
        continue

    if index == 127 or False in occupied_seats[index + 1]:
        continue

    if False in row:
        column = row.index(False)
        print(f"free seat at row {index}, column {column}, id {index * 8 + column}")

# %%
# it printed:
# free seat at row 66, column 4, id 532


# THE MOST ELEGANT WAY:
# it works because the seat codes are just binary number strings
# replacing 0 and 1 with letters.


def get_seat_id(seat_code):
    binary_string = (
        seat_code.replace("F", "0")
        .replace("L", "0")
        .replace("B", "1")
        .replace("R", "1")
    )
    return int(binary_string, 2)


with open("input.txt") as f:
    seat_ids = [get_seat_id(seat_code) for seat_code in f.read().split("\n")]

max_id = max(seat_ids)
min_id = min(seat_ids)

print(f"max:{max_id} min:{min_id}")

# no need to build plane
for i in range(min_id, max_id):
    if i not in seat_ids:
        print(f"seat with id {i} is empty")

# %%
