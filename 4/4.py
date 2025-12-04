from pkg.handle_test import run_solution as runner

def sol_p1(input):
    rolls = [] 
    adjacent_rolls = [[0 for x in range(len(input))] for y in range(len(input[0]))]
    max_rows = len(input)
    max_cols = len(input[0])

    for row_index in range(max_rows):
        row = input[row_index]
        for col_index in range(max_cols):
            item = input[row_index][col_index]
            if item == '@':
                rolls.append((row_index, col_index))
                for i in range(row_index - 1, row_index + 2):
                    for j in range(col_index - 1, col_index + 2):
                        if i == row_index and j == col_index:
                            # ignore self
                            continue
                        if i >= 0 and i < max_rows and j >= 0 and j < max_cols:
                            adjacent_rolls[i][j] += 1
         
    acc = 0
    for roll_coord in rolls:
        if adjacent_rolls[roll_coord[0]][roll_coord[1]] < 4:
            acc += 1
    return acc

def sol_p2(input):
    max_rows = len(input)
    max_cols = len(input[0])
    roll_map = input

    removing_rolls = True
    acc = 0
    while removing_rolls:
        rolls = [] 
        adjacent_rolls = [[0 for x in range(len(input))] for y in range(len(input[0]))]
        roll_map, num_removed = remove_rolls(roll_map, rolls, adjacent_rolls, max_rows, max_cols)
        acc += num_removed
        if num_removed == 0:
            removing_rolls = False
    
    return acc

def remove_rolls(roll_map, rolls, adj_rolls, max_rows, max_cols):    
    for row_index in range(max_rows):
        for col_index in range(max_cols):
            item = roll_map[row_index][col_index]
            if item == '@':
                rolls.append((row_index, col_index))
                for i in range(row_index - 1, row_index + 2):
                    for j in range(col_index - 1, col_index + 2):
                        if i == row_index and j == col_index:
                            # ignore self
                            continue
                        if i >= 0 and i < max_rows and j >= 0 and j < max_cols:
                            adj_rolls[i][j] += 1
    acc = 0
    for roll_coord in rolls:
        if adj_rolls[roll_coord[0]][roll_coord[1]] < 4:
            acc += 1 
            roll_map[roll_coord[0]] = roll_map[roll_coord[0]][:roll_coord[1]] + '.' + roll_map[roll_coord[0]][roll_coord[1]+1:]
    return roll_map, acc 


runner(sol_p2, 4, '/testcases/2', '/q/q.txt')