with open('input/day3.txt', 'r') as f:
    raster = [line.replace('\n', '') for line in f]

broadth = len(raster[0])
length = len(raster)
final_answer = 1

trajectories = [[1,1],[1,3],[1,5],[1,7],[2,1]]

print('=== PART #1 ===')
for t in trajectories:
    x_coord = 0
    y_coord = 0
    tree_counter = 0
    for y in range(0,length,t[0]):
        if raster[y][x_coord] == '#':
            tree_counter += 1
        x_coord = (x_coord + t[1]) % broadth

    print(f'{tree_counter} trees with trajectory {t}')
    final_answer *= tree_counter

print('=== PART #2 ===')
print(f'The final product is: {final_answer}')
