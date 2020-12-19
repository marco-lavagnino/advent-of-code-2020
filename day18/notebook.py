#%%

import re
from operator import add, mul

operations = {
    "*": mul,
    "+": add,
}


def solve_math(math_string):
    try:
        return int(math_string)
    except ValueError:
        pass

    expression, op, num = re.search(r"(.*)([\+\*])(\d+)", math_string).groups()

    return operations[op](int(num), solve_math(expression))


def solve_expression(expr):
    expr = expr.replace(" ", "")

    while "(" in expr:

        expr = re.sub(
            r"\([^\(^\).]+\)", lambda s: str(solve_math(s.group(0)[1:-1])), expr
        )

    return solve_math(expr)


assert solve_expression("2 * 3 + (4 * 5)") == 26
assert solve_expression("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert solve_expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert solve_expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632


def part_one():
    with open("input.txt") as f:
        return sum(solve_expression(s) for s in f.read().split("\n"))


part_one()


#%%


def solve_mul(expr):
    if "*" not in expr:
        return sum(int(i) for i in expr.split("+"))

    expr1, op, expr2 = expr.partition("*")

    return solve_mul(expr1) * solve_mul(expr2)


def solve_expression_2(expr):
    expr = expr.replace(" ", "")

    while "(" in expr:

        expr = re.sub(
            r"\([^\(^\).]+\)", lambda s: str(solve_mul(s.group(0)[1:-1])), expr
        )

    return solve_mul(expr)


assert solve_expression_2("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert solve_expression_2("2 * 3 + (4 * 5)") == 46
assert solve_expression_2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
assert solve_expression_2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
assert solve_expression_2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340


def part_two():
    with open("input.txt") as f:
        return sum(solve_expression_2(s) for s in f.read().split("\n"))


part_two()
# %%
