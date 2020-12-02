#%%

with open("input.txt") as f:
    lines = [line.replace("-", " ").replace(":", "").split() for line in f.readlines()]

# %%
valid = 0

for min, max, letter, password in lines:
    if int(min) <= password.count(letter) <= int(max):
        valid += 1

valid

# %%
valid = 0

for pos1, pos2, letter, password in lines:
    a = password[int(pos1) - 1] == letter
    b = password[int(pos2) - 1] == letter
    if a != b:
        valid += 1

valid
