f = open('input/day7.txt').read().splitlines()

rules = []
def parse_input(rule: str):
    rule_dict = dict()
    rule = rule.replace('bags', '').replace('bag', '').replace('.', '')
    rule = rule.split('contain')
    rule_dict['outer_bag'] = rule[0].strip()
    rule_dict['inner_bags'] = [inner_bag.strip().split(' ', 1)[1] for inner_bag in rule[1].split(', ')]
    return rule_dict

[rules.append(parse_input(rule)) for rule in f]
#print(parse_input(f[0]))


possible_bags = {'shiny gold'}
old_length = len(possible_bags)

while True:
    for rule in rules:
        if bool(set(possible_bags) & set(rule['inner_bags'])): #not possible_bags.isdisjoint(rule['inner_bags']):
            possible_bags.add(rule['outer_bag'])
    if old_length == len(possible_bags):
        break
    else:
        old_length = len(possible_bags)

print(f'The amount of possible bags is {len(possible_bags)}')