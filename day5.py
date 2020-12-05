f = open('input/day5.txt').read().splitlines()

def decode_seat(code: str):
    row = range(128)
    seat = range(8)

    for i in range(7):
        middleIndex = len(row)//2
        if code[i] == 'F':
            row = row[:middleIndex]
        elif code[i] == 'B':
            row = row[middleIndex:]

    for i in range(7,10):
        middleIndex = len(seat)//2
        if code[i] == 'L':
            seat = seat[:middleIndex]
        elif code[i] == 'R':
            seat = seat[middleIndex:]
    
    return(row[0], seat[0])
    
def calc_seat_ID(seat: tuple):
    return seat[0] * 8 + seat[1]

def print_seat_info(seat: tuple):
    id = calc_seat_ID(seat)
    print(f'Row {seat[0]}, Seat {seat[1]}, ID {id}')

def find_empty_seat(all_IDs: list):
    previous_ID = all_IDs[0]-1

    for id in all_IDs:
        if previous_ID + 1 == id:
            previous_ID = id
        else:
            return previous_ID + 1


highest_ID = 0
for boarding_pass in f:
    current_ID = calc_seat_ID(decode_seat(boarding_pass))
    highest_ID =  current_ID if current_ID > highest_ID else highest_ID 

all_IDs = []
for boarding_pass in f:
    all_IDs.append(calc_seat_ID(decode_seat(boarding_pass)))
all_IDs.sort()

my_seat = find_empty_seat(all_IDs)


print('=== PART #1 ===')
print(f'The highest Boarding Pass ID is {highest_ID}')

print('=== PART #2 ===')
print(f'My seat is Boarding Pass ID {my_seat}')