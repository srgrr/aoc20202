import re

blank_regex = re.compile(r'(?:\n){2,}')

passports = re.split(blank_regex, open('input.txt', 'r').read().strip())

valid_passports = 0


def byr_rule(x):
    byr_regex = re.compile(r'^([0-9]{4})$')
    match = re.match(byr_regex, x)
    if match is not None:
        val = int(match.group(1))
        return val >= 1920 and val <= 2002
    return False


def iyr_rule(x):
    iyr_regex = re.compile(r'^([0-9]{4})$')
    match = re.match(iyr_regex, x)
    if match is not None:
        val = int(match.group(1))
        return val >= 2010 and val <= 2020
    return False


def eyr_rule(x):
    eyr_regex = re.compile(r'^([0-9]{4})$')
    match = re.match(eyr_regex, x)
    if match is not None:
        val = int(match.group(1))
        return val >= 2020 and val <= 2030
    return False


def height_rule(x):
    height_regex = re.compile(r'^([0-9]+)(cm|in)$')
    match = re.match(height_regex, x)
    if match is not None and len(match.groups()) == 2:
        height, units = int(match.group(1)), match.group(2)
        if units == 'cm':
            return height >= 150 and height <= 193
        return height >= 59 and height <= 76
    return False


def hcl_rule(x):
    hcl_regex = re.compile(r'^#[0-9a-f]{6}$')
    return re.match(hcl_regex, x) is not None


def pid_rule(x):
    pid_regex = re.compile(r'^[0-9]{9}$')
    return re.match(pid_regex, x) is not None


rules = {
    'byr': byr_rule,
    'iyr': iyr_rule,
    'eyr': eyr_rule,
    'hgt': height_rule,
    'hcl': hcl_rule,
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': pid_rule,
    'cid': lambda x: True
}


for passport in [x.replace('\n', ' ') for x in passports]:
    missing_fields = \
        set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
    is_valid = True
    for field in passport.split(' '):
        name, value = field.split(':')
        is_valid = is_valid and rules[name](value)
        missing_fields.remove(name)
    if is_valid and (not missing_fields or missing_fields == set(['cid'])):
        valid_passports += 1


print(valid_passports)
