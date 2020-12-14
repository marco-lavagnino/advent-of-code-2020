# https://adventofcode.com/2020/day/14
#%%
with open("sample.txt") as f:
    sample_lines = f.read().split("\n")

with open("input.txt") as f:
    input_lines = f.read().split("\n")

with open("sample2.txt") as f:
    sample2_lines = f.read().split("\n")

# %%
import re


def part_one(lines):
    memory = {}
    for line in lines:
        if line[:4] == "mask":
            mask = line[7:]
            and_mask = int("".join(("0" if x == "0" else "1" for x in mask)), 2)
            or_mask = int("".join(("1" if x == "1" else "0" for x in mask)), 2)
        else:
            address, num = re.findall(r"mem\[(\d+)\] = (\d+)", line)[0]
            memory[address] = (int(num) | or_mask) & and_mask

    return sum(memory.values())


assert part_one(sample_lines) == 165

part_one(input_lines)

# %%

import re


def part_two(lines):

    or_mask = None
    x_masks = None

    def get_addresses(original_address):
        addresses = [original_address | or_mask]
        for x_mask in x_masks:
            addresses += [addr ^ x_mask for addr in addresses]
        return addresses

    memory = {}

    for line in lines:
        if line[:4] == "mask":
            mask = line[7:]
            or_mask = int("".join(("1" if x == "1" else "0" for x in mask)), 2)
            x_masks = [
                int("".join(("1" if i == index else "0" for i in range(len(mask)))), 2)
                for index, char in enumerate(mask)
                if char == "X"
            ]
        else:
            original_address, num = re.findall(r"mem\[(\d+)\] = (\d+)", line)[0]
            for address in get_addresses(int(original_address)):
                memory[address] = int(num)

    return sum(memory.values())


assert part_two(sample2_lines) == 208

part_two(input_lines)

# %%
