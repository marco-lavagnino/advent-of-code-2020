# https://adventofcode.com/2020/day/4
#%%
with open("sample.txt") as f:
    blocks = [
        dict((tag.split(":") for tag in ss.replace("\n", " ").split()))
        for ss in f.read().split("\n\n")
    ]

blocks

#%%
with open("input.txt") as f:
    blocks = [
        dict((tag.split(":") for tag in ss.replace("\n", " ").split()))
        for ss in f.read().split("\n\n")
    ]


# %%
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid = 0
for block in blocks:
    if required_fields <= set(block.keys()):
        valid += 1

valid

#
# PART 2
#

#%%
with open("invalid_values.txt") as f:
    blocks = [
        dict((tag.split(":") for tag in ss.replace("\n", " ").split()))
        for ss in f.read().split("\n\n")
    ]

#%%
with open("valid_values.txt") as f:
    blocks = [
        dict((tag.split(":") for tag in ss.replace("\n", " ").split()))
        for ss in f.read().split("\n\n")
    ]


# %%


def validate_year(value, min, max):
    assert min <= int(value) <= max


def validate_height(value):
    assert len(value) > 2

    unit = value[-2:]
    amount = value[:-2]

    if unit == "cm":
        assert 150 <= int(amount) <= 193
    elif unit == "in":
        assert 59 <= int(amount) <= 76
    else:
        raise AssertionError


import re


def validate_hair(value):
    assert re.match(r"#[0-9a-f]{6}$", value)


def validate_eyes(value):
    assert value in (
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    )


def validate_passport(value):
    assert re.match(r"\d{9}$", value)


# testing


def passes_validation(validation, value):
    try:
        validation(value)
    except:
        return False
    return True


assert passes_validation(validate_height, "60in")
assert passes_validation(validate_height, "190cm")
assert not passes_validation(validate_height, "190in")
assert not passes_validation(validate_height, "190")

assert passes_validation(validate_hair, "#123abc")
assert not passes_validation(validate_hair, "#123abz")
assert not passes_validation(validate_hair, "123abc")

assert passes_validation(validate_eyes, "brn")
assert not passes_validation(validate_eyes, "wat")

assert passes_validation(validate_passport, "000000001")
assert not passes_validation(validate_passport, "0123456789")


valid = 0
for block in blocks:
    try:
        validate_year(block["byr"], 1920, 2002)
        validate_year(block["iyr"], 2010, 2020)
        validate_year(block["eyr"], 2020, 2030)
        validate_height(block["hgt"])
        validate_hair(block["hcl"])
        validate_eyes(block["ecl"])
        validate_passport(block["pid"])

        valid += 1
    except (KeyError, ValueError, AssertionError):
        pass

valid
# %%
