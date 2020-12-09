#%%
from itertools import combinations

with open("sample.txt") as f:
    numbers = [int(n) for n in f.read().split("\n")]


WINDOW = 5

for i in range(WINDOW, len(numbers)):
    check = numbers[i - WINDOW : i]

    assert any((numbers[i] == a + b for a, b in combinations(check, 2))), numbers[i]


#%%
from itertools import combinations

with open("input.txt") as f:
    numbers = [int(n) for n in f.read().split("\n")]


WINDOW = 25

for i in range(WINDOW, len(numbers)):
    check = numbers[i - WINDOW : i]

    assert any((numbers[i] == a + b for a, b in combinations(check, 2))), numbers[i]

# %%

with open("sample.txt") as f:
    numbers = [int(n) for n in f.read().split("\n")]

FOUND_NUM = 127

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        total = sum(numbers[i:j])

        if total >= FOUND_NUM:
            break

    if total == FOUND_NUM:
        break

minimum = min(numbers[i:j])
maximum = max(numbers[i:j])

minimum + maximum

# %%

with open("input.txt") as f:
    numbers = [int(n) for n in f.read().split("\n")]

FOUND_NUM = 26134589

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        total = sum(numbers[i:j])

        if total >= FOUND_NUM:
            break

    if total == FOUND_NUM:
        break

minimum = min(numbers[i:j])
maximum = max(numbers[i:j])

minimum + maximum

# %%
