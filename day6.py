# Day 6: Trash Compactor

def solve_worksheet_left_to_right(worksheet_text):
    lines = worksheet_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = max(len(line) for line in lines)
    for i in range(rows):
        while len(grid[i]) < cols:
            grid[i].append(' ')
    column_groups = []
    current_group = []
    
    for col_i in range(cols):
        is_space_column = all(grid[row][col_i] == ' ' for row in range(rows))
        if is_space_column:
            if current_group:
                column_groups.append(current_group)
                current_group = []
        else:
            current_group.append(col_i)
    if current_group:
        column_groups.append(current_group)
    results = []
    for group_i, col_indices in enumerate(column_groups):
        operator = None
        for col_i in col_indices:
            char = grid[-1][col_i]
            if char in ['+', '*']:
                operator = char
                break        
        numbers = []
        for col_i in col_indices:
            digits = []
            for row_idx in range(rows - 1): 
                cell = grid[row_idx][col_i]
                if cell.isdigit():
                    digits.append(cell)
            if digits:
                number = int(''.join(digits))
                numbers.append(number)
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for num in numbers:
                result *= num        
        results.append(result)
    return sum(results)

def solve_worksheet_right_to_left(worksheet_text):
    lines = worksheet_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = max(len(line) for line in lines)
    for i in range(rows):
        while len(grid[i]) < cols:
            grid[i].append(' ')
    column_groups = []
    current_group = []
    
    for col_i in range(cols):
        is_space_column = all(grid[row][col_i] == ' ' for row in range(rows))
        if is_space_column:
            if current_group:
                column_groups.append(current_group)
                current_group = []
        else:
            current_group.append(col_i)
    if current_group:
        column_groups.append(current_group)
    column_groups.reverse()
    results = []
    
    for group_i, col_indices in enumerate(column_groups):
        operator = None
        for col_i in col_indices:
            char = grid[-1][col_i]
            if char in ['+', '*']:
                operator = char
                break
        numbers = []
        for col_i in col_indices:
            digits = []
            for row_i in range(rows - 1):
                cell = grid[row_i][col_i]
                if cell.isdigit():
                    digits.append(cell)
            if digits:
                number = int(''.join(digits))
                numbers.append(number)
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for num in numbers:
                result *= num
        results.append(result)
    return sum(results)

def solve_cephalopod_worksheet(worksheet_text):
    result_ltr = solve_worksheet_left_to_right(worksheet_text)    
    result_rtl = solve_worksheet_right_to_left(worksheet_text)    
    return result_ltr, result_rtl

worksheet = """"""

result_part1, result_part2 = solve_cephalopod_worksheet(worksheet)
print(f"Left-to-right: {result_part1}")
print(f"Right-to-left: {result_part2}")