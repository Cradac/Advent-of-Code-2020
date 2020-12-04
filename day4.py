from collections import Counter
from re import match

batch = []
with open('input/day4.txt', 'r') as f:
    raw = [line.replace('\n', '') for line in f]
    pre_proc = []
    current = ''
    for line in raw:
        if line != '':
            current += line + ' '
        else:
            pre_proc.append(current)
            current = ''

    for line in pre_proc:
        dict = {}
        line = line.split(' ')
        line.remove('')
        for entry in line:
            entry = entry.split(':')
            dict[entry[0]] = entry[1]
        batch.append(dict)

req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #'cid'
req = Counter(req)

ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

counter1 = 0
counter2 = 0

for passport in batch:
    passport.pop('cid', None)
    if Counter(passport.keys()) == req:
        counter1 += 1
        if 1920 <= int(passport['byr']) <= 2002 and 2010 <= int(passport['iyr']) <= 2020 and 2020 <= int(passport['eyr']) <= 2030:
            if (passport['hgt'].endswith('in') and 59 <= int(passport['hgt'].replace('in', '')) <= 76) or (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'].replace('cm', '')) <= 193):
                if match(r'#[a-f|0-9]{6}', passport['hcl']):
                    passport['hcl']
                    if passport['ecl'] in ecl:
                        if match(r'[0-9]{9}', passport['pid']):
                            counter2 += 1

print('=== PART #1 ===')
print(f'This many passports are valid: {counter1}')
print('=== PART #2 ===')
print(f'This many passports are valid: {counter2}')
