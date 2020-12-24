#%%

from functools import cache
import re


def parse_file(filename):
    with open(filename) as f:
        rules_block, messages_block = f.read().split("\n\n")

    rules = {
        int(key): [
            [eval(rule) for rule in rule_seq.split()] for rule_seq in value.split("|")
        ]
        for key, value in (line.split(": ") for line in rules_block.split("\n"))
    }

    messages = messages_block.split("\n")

    return rules, messages


def part_one(filename):
    rules, messages = parse_file(filename)

    @cache
    def regex_rule(rule_num):
        if type(rules[rule_num][0][0]) == str:
            return rules[rule_num][0][0]

        return (
            "("
            + r"|".join(
                r"".join(regex_rule(i) for i in rule_seq)
                for rule_seq in rules[rule_num]
            )
            + ")"
        )

    regex = re.compile(regex_rule(0) + "$")

    return sum(1 for message in messages if regex.match(message))


part_one("input.txt")

# regex_rule(0)

# %%


def part_two(filename):
    rules, messages = parse_file(filename)

    @cache
    def regex_rule(rule_num):
        if rule_num == 8:
            # 42 | 42 8
            return f"({regex_rule(42)}+)"

        if rule_num == 11:
            # 42 31 | 42 11 31
            return (
                "("
                + "|".join(
                    f"({regex_rule(42)}{{{i}}}{regex_rule(31)}{{{i}}})"
                    for i in range(1, 10)
                )
                + ")"
            )

        if type(rules[rule_num][0][0]) == str:
            return rules[rule_num][0][0]

        return (
            "("
            + r"|".join(
                r"".join(regex_rule(i) for i in rule_seq)
                for rule_seq in rules[rule_num]
            )
            + ")"
        )

    regex = re.compile(regex_rule(0) + "$")

    assert regex.match("bbabbbbaabaabba")
    assert regex.match("babbbbaabbbbbabbbbbbaabaaabaaa")
    assert regex.match("aaabbbbbbaaaabaababaabababbabaaabbababababaaa")
    assert regex.match("bbbbbbbaaaabbbbaaabbabaaa")
    assert regex.match("bbbababbbbaaaaaaaabbababaaababaabab")
    assert regex.match("ababaaaaaabaaab")
    assert regex.match("ababaaaaabbbaba")
    assert regex.match("baabbaaaabbaaaababbaababb")
    assert regex.match("abbbbabbbbaaaababbbbbbaaaababb")
    assert regex.match("aaaaabbaabaaaaababaa")
    assert regex.match("aaaabbaabbaaaaaaabbbabbbaaabbaabaaa")
    assert regex.match("aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba")

    return sum(1 for message in messages if regex.match(message))


# part_two("sample2.txt")
part_two("input.txt")

# %%
