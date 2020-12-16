#%%

import re


def parse_ticket_line(ticket_line):
    return [int(i) for i in ticket_line.split(",")]


def parse_file(filename):
    with open(filename) as f:
        raw_rules, raw_my_ticket, raw_nearby = f.read().split("\n\n")

    rules = {
        rule_name: [range(int(a), int(b) + 1), range(int(c), int(d) + 1)]
        for rule_name, a, b, c, d in re.findall(
            r"([ \w]+): (\d+)-(\d+) or (\d+)-(\d+)", raw_rules
        )
    }

    my_ticket = parse_ticket_line(raw_my_ticket.split("\n")[1])

    nearby_tickets = [parse_ticket_line(line) for line in raw_nearby.split("\n")[1:]]

    return rules, my_ticket, nearby_tickets


parse_file("sample.txt")
# %%
from itertools import chain


def part_one(parsed):
    rules, _, nearby_tickets = parsed

    ranges = list(chain.from_iterable(rule_pair for rule_pair in rules.values()))

    return sum(
        i
        for i in chain.from_iterable(nearby_tickets)
        if not any(i in num_range for num_range in ranges)
    )


assert part_one(parse_file("sample.txt")) == 71

part_one(parse_file("input.txt"))

# %%
from functools import reduce
from operator import mul


def part_two():
    rules, my_ticket, nearby_tickets = parse_file("input.txt")

    ranges = list(chain.from_iterable(rule_pair for rule_pair in rules.values()))

    def ticket_is_valid(ticket):
        return all(any(i in num_range for num_range in ranges) for i in ticket)

    possible_fields = [set(rules.keys()) for _ in my_ticket]

    # horrible complexity
    for ticket in nearby_tickets:
        if not ticket_is_valid(ticket):
            continue

        for index, num in enumerate(ticket):
            for possible_field in list(possible_fields[index]):
                if (num not in rules[possible_field][0]) and (
                    num not in rules[possible_field][1]
                ):
                    possible_fields[index].remove(possible_field)

    # horrible complexity again
    while any((len(possible_field) > 1 for possible_field in possible_fields)):
        for i, possible_field in enumerate(possible_fields):
            if len(possible_field) != 1:
                continue

            for j, other_field in enumerate(possible_fields):
                if i != j:
                    possible_fields[j] = other_field - possible_field

    return reduce(
        mul,
        (
            num
            for index, num in enumerate(my_ticket)
            if (
                possible_fields[index]  # some fields are not used, this filters them
                and "departure" in next(iter(possible_fields[index]))
            )
        ),
    )


# there are no test for sample data
part_two()

# %%
