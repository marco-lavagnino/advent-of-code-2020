#%%
sample_n = 939
sample_list = "7,13,x,x,59,x,31,19".split(",")

input_n = 1001796
input_list = "37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,457,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,431,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19".split(
    ","
)

# %%


def part_one(n, service_list):
    input = [int(i) for i in service_list if i != "x"]

    departure_times = {i: i * ((n // i) + 1) for i in input}

    num, time = min(departure_times.items(), key=(lambda t: t[1]))

    return num * (time - n)


assert part_one(sample_n, sample_list) == 295
part_one(input_n, input_list)

# %%

"""
Instead of using the chinese remainder theorem as this was intended,
I thought this was solved using diophantine equations.

I found a library that solved diophantine equations, to run this you'll
need to install it

>> pip install diophantine

However, the lib sometimes returns negative values. To get a positive value
like the problem requires, I downloaded the relevant file from the lib
and patched it.

This is extremely hacky! Never do this.
"""


from my_diophantine import solve, ShamefulHack


def part_two(service_list):
    idx = [(index, int(num)) for index, num in enumerate(service_list) if num != "x"]

    A = [[0 for _ in range(len(idx) + 1)] for _ in range(len(idx))]

    for index, (offset, num) in enumerate(idx):
        A[index][index] = num
        A[index][-1] = -1

    b = [index for index, num in idx]

    try:
        return int(solve(A, b)[0][-1])
    except ShamefulHack as e:
        return int(e.args[0])


assert part_two("17,x,13,19".split(",")) == 3417
assert part_two("67,7,59,61".split(",")) == 754018
assert part_two("67,x,7,59,61".split(",")) == 779210
assert part_two("67,7,x,59,61".split(",")) == 1261476
assert part_two("1789,37,47,1889".split(",")) == 1202161486


part_two(sample_list)
part_two(input_list)
# %%
