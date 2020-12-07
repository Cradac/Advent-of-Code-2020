f = open('input/day6.txt').read().splitlines()

sum_counts = 0
group = set()
for answer in f:
    if answer != '':
        for char in answer:
            group.add(char)
    if answer == '':
        sum_counts += len(group)
        group = set()
sum_counts += len(group)

print('=== PART #1 ===')
print(f'The sum of "yes" answers on a question per group is: {sum_counts}')


flag = True
group = set()
sum_counts = 0
for answer in f:
    if answer != '' and flag:
        group = set(answer)
        flag = False
    elif answer != '' and not flag:
        group = group.intersection(set(answer))
    if answer == '':
        sum_counts += len(group)
        group = set()
        flag = True

sum_counts += len(group)
print('=== PART #2 ===')
print(f'The sum of "yes" answers on a question from everyone in a group is: {sum_counts}')
