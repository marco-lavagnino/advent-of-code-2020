#%%

memo = [0, 3, 6]
memo = [7, 12, 1, 0, 16, 2]

while len(memo) < 2020:
    last_num = memo[-1]
    gen = (index for index, num in reversed(list(enumerate(memo))) if num == last_num)

    last_index = next(gen)
    try:
        prev_index = next(gen)
    except StopIteration:
        memo.append(0)
        continue
    memo.append(last_index - prev_index)

memo[-1]
# %%


memo = [0, 3, 6]
memo = [7, 12, 1, 0, 16, 2]

last_appeared = {num: index for index, num in enumerate(memo[:-1])}
last_num = memo[-1]

N = 30000000

for i in range(len(memo), N):
    try:
        new_num = i - 1 - last_appeared[last_num]
    except KeyError:
        new_num = 0

    last_appeared[last_num] = i - 1
    last_num = new_num

last_num
# %%
