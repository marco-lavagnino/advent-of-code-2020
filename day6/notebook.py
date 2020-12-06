#%%
with open("sample.txt") as f:
    groups = [s.split("\n") for s in f.read().split("\n\n")]
sum(len(set("".join(group))) for group in groups)

# %%
with open("input.txt") as f:
    groups = [s.split("\n") for s in f.read().split("\n\n")]

sum(len(set("".join(group))) for group in groups)
# %%
# PART TWO

#%%
from functools import reduce

with open("sample.txt") as f:
    groups = [s.split("\n") for s in f.read().split("\n\n")]

sum(
    [
        len(reduce((lambda x, y: x.intersection(y)), [set(x) for x in group]))
        for group in groups
    ]
)
# %%

#%%
from functools import reduce

with open("input.txt") as f:
    groups = [s.split("\n") for s in f.read().split("\n\n")]

sum(
    [
        len(reduce((lambda x, y: x.intersection(y)), [set(x) for x in group]))
        for group in groups
    ]
)
# %%
