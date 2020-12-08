#%%
with open("sample.txt") as f:
    lines = f.read()

#%%
with open("input.txt") as f:
    lines = f.read()

#%%
# PART ONE
import re

instructions = re.findall(r"(\w+) ([\-\+])(\d+)", lines)
visited = [False for _ in instructions]

counter = 0
value = 0

while not visited[counter]:
    visited[counter] = True

    opcode, sign, num = instructions[counter]

    number = int(num)
    if sign == "-":
        number = -number

    if opcode == "jmp":
        counter += number
    else:
        counter += 1

        if opcode == "acc":
            value += number

value

# %%
# PART TWO


def run(instructions):
    visited = [False for _ in instructions]

    counter = 0
    value = 0

    while counter < len(instructions) and not visited[counter]:
        visited[counter] = True

        opcode, sign, num = instructions[counter]

        number = int(num)
        if sign == "-":
            number = -number

        if opcode == "jmp":
            counter += number
        else:
            counter += 1

            if opcode == "acc":
                value += number

    finished = counter >= len(instructions)
    return finished, value


instructions = re.findall(r"(\w+) ([\-\+])(\d+)", lines)

for index, (opcode, sign, num) in enumerate(instructions):
    if opcode == "acc":
        continue

    swap = {
        "jmp": "nop",
        "nop": "jmp",
    }

    new_instructions = instructions.copy()
    new_instructions[index] = (swap[opcode], sign, num)

    finished, value = run(new_instructions)

    if finished:
        print(f"value: {value}")
        break
# %%
