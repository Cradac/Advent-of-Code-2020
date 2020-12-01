i = open("input/day1.txt", "r")
i = i.read().split('\n')
i = [int(x) for x in i]

flag = False

print('=== PART #1 ===')
for first in i:
    for second in i:
        if first + second == 2020: 
            print(f'first: {first}; second: {second}; equals: {first + second}')
            flag = True
            break
    if flag: break

print(first*second)

print('=== PART #2 ===')

flag = False
for first in i:
    for second in i:
        for third in i:
            if first + second + third == 2020: 
                print(f'first: {first}; second: {second}; third: {third}; equals: {first + second + third}')
                flag = True
                break
        if flag: break
    if flag: break

print(first*second*third)
#if __name__ == "__main__":
    #pass