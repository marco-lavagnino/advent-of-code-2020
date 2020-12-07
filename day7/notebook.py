#%%
with open("sample.txt") as f:
    lines = f.read().split("\n")

#%%
with open("input.txt") as f:
    lines = f.read().split("\n")

# %%
# parse lines
import re
from collections import defaultdict


dependencies = {}
reverse_deps = defaultdict(dict)


for line in lines:
    color = re.findall(r"^(\w+ \w+) bags", line)[0]
    deps = re.findall(r"(\d+) (\w+ \w+) bags?", line)

    dependencies[color] = {color_name: int(number) for number, color_name in deps}

    for num, contained_color in deps:
        reverse_deps[contained_color][color] = int(num)


# %%
# PART 1
# colors that can contain my bag
accepted = set()
colors_to_check = ["shiny gold"]


for color in colors_to_check:
    for containing_color in reverse_deps[color].keys():
        if containing_color not in accepted:
            accepted.add(containing_color)
            # warning: I'm appending to list I'm currently iterating
            colors_to_check.append(containing_color)

# bag colors that can contain my bag
len(accepted)

# %%
# PART 2


def contained_bags(color):
    return sum(
        [
            number + contained_bags(contained_color) * number
            for contained_color, number in dependencies[color].items()
        ]
    )


contained_bags("shiny gold")
# %%
