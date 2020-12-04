import re

blank_regex = re.compile(r'(?:\n){2,}')

passports = re.split(blank_regex, open('input.txt', 'r').read().strip())

valid_passports = 0

for passport in [x.replace('\n', ' ') for x in passports]:
    missing_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
    for field in passport.split(' '):
        missing_fields.remove(field.split(':')[0])
    if not missing_fields or missing_fields == set(['cid']):
        valid_passports += 1

print(valid_passports)
