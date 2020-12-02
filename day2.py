from typing import Counter


i = open("input/day2.txt", "r")
i = i.read().split('\n')

counter = 0
counter_2 = 0




for entry in i:
    policy, password = entry.split(': ')
    times, char = policy.split(' ')
    min_times, max_times = times.split('-')

    if int(min_times) <= password.count(char) <= int(max_times):
        counter += 1

    idx1 = int(min_times) - 1
    idx2 = int(max_times) - 1

    if (password[idx1] == char and not password[idx2] == char) or (not password[idx1] == char and password[idx2] == char):
        counter_2 += 1


print('=== PART #1 ===')
print(f'amount of valid passwords: {counter}')
print('=== PART #2 ===')
print(f'amount of valid passwords: {counter_2}')
