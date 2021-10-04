instructions = open('input/day8.txt').read().splitlines()

def clone(li1): 
    return li1[:] 

def jmp(var: int, index: int):
    return index + var


def acc(var: int, index: int, accumulator: int):
    return index + 1, accumulator + var

def decode(line: str, index: int, accumulator: int):

    instruction, value = line.split(' ')
    value = int(value)

    if instruction == 'nop':
        index = jmp(1, index)
    elif instruction == 'acc':
        index, accumulator = acc(value, index, accumulator)
    elif instruction == 'jmp':
        index = jmp(value, index) 
    elif line == '':
        return index, accumulator
    #print(f'{line} | {accumulator}')
    return index, accumulator

history = set()
accumulator = 0
index = 0

while index not in history:
    history.add(index)
    index , accumulator = decode(instructions[index], index, accumulator)

print('=== PART #1 ===')
print(f'The value of the accumulator before the loop is {accumulator}')

print('=== PART #2 ===')

for outer_index in range(len(instructions)):
    cur_instruct = instructions[outer_index].split(' ')[0]
    #cur_instruct = cur_instruct
    #print(cur_instruct)
    cur_instructs = clone(instructions)
    if cur_instruct not in ['nop', 'jmp']:
        continue
    elif cur_instruct == 'nop':
        #print(cur_instructs[outer_index])
        cur_instructs[outer_index] = cur_instructs[outer_index].replace('nop', 'jmp')
        #print(cur_instructs[outer_index])
    elif cur_instruct == 'jmp':
        #print(cur_instructs[outer_index])
        cur_instructs[outer_index] = cur_instructs[outer_index].replace('jmp', 'nop')
        #print(cur_instructs[outer_index])
    #print('===')
    #print(cur_instructs)
    #print('****')
    history = set()
    accumulator = 0
    index = 0

    while index not in history:
        history.add(index)
        index , accumulator = decode(cur_instructs[index], index, accumulator)
        if index == len(instructions):
            break
    if index == len(instructions):
        break
        

print(f'The value of the accumulator if the program runs smoothly is {accumulator}')
