matrix = [list(line) for line in open("input.txt", "r").read().splitlines()]

direction_map = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def move(direction, pos):
    matrix[pos[0]][pos[1]] = 'X'
    
    offsets = {'^': (-1, 0), '<': (0, -1), '>': (0, 1), 'v': (1, 0)}
    new_pos = [pos[0] + offsets[direction][0], pos[1] + offsets[direction][1]]
    
    # Check if the new position is within bounds
    if not (0 <= new_pos[0] < len(matrix)) or not (0 <= new_pos[1] < len(matrix[0])):
        return "NONE", new_pos

    if matrix[new_pos[0]][new_pos[1]] != '#':
        matrix[new_pos[0]][new_pos[1]] = direction
        return direction, new_pos
    else: #only turn, no movement
        direction = direction_map.get(direction)
        return direction, pos  

direction = "^"
pos = next((r, row.index(direction)) for r, row in enumerate(matrix) if direction in row)
while direction != "NONE": direction, pos = move(direction, pos)
print(sum(row.count('X') for row in matrix))
