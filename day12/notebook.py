# https://adventofcode.com/2020/day/11
#%%
import re


def get_state_from_file(filename):
    with open(filename) as f:
        return [(a, int(b)) for a, b in re.findall(r"(\w)(\d+)", f.read())]


sample = get_state_from_file("sample.txt")
input = get_state_from_file("input.txt")


# %%
from math import sin, cos, radians


def part_one(instructions):
    degrees = 0
    x = 0
    y = 0

    for instruction_char, number in instructions:
        if instruction_char == "N":
            y += number
        if instruction_char == "S":
            y -= number
        if instruction_char == "E":
            x += number
        if instruction_char == "W":
            x -= number
        if instruction_char == "L":
            degrees += number
        if instruction_char == "R":
            degrees -= number
        if instruction_char == "F":
            x += round(cos(radians(degrees)) * number)
            y += round(sin(radians(degrees)) * number)

    return abs(x) + abs(y)


assert part_one(sample) == 25

part_one(input)
# %%


def part_two(instructions):
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1

    for instruction_char, number in instructions:
        if instruction_char == "N":
            waypoint_y += number
        if instruction_char == "S":
            waypoint_y -= number
        if instruction_char == "E":
            waypoint_x += number
        if instruction_char == "W":
            waypoint_x -= number
        if instruction_char == "L":
            waypoint_x, waypoint_y = (
                round(
                    cos(radians(number)) * waypoint_x
                    - sin(radians(number)) * waypoint_y
                ),
                round(
                    sin(radians(number)) * waypoint_x
                    + cos(radians(number)) * waypoint_y
                ),
            )
        if instruction_char == "R":
            waypoint_x, waypoint_y = (
                round(
                    cos(radians(-number)) * waypoint_x
                    - sin(radians(-number)) * waypoint_y
                ),
                round(
                    sin(radians(-number)) * waypoint_x
                    + cos(radians(-number)) * waypoint_y
                ),
            )
        if instruction_char == "F":
            ship_x += waypoint_x * number
            ship_y += waypoint_y * number

    return abs(ship_x) + abs(ship_y)


assert part_two(sample) == 286
part_two(input)

# %%
