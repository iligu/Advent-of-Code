#Day 4: Printing Department

def count_accessible_rolls_once(grid_text):
    lines = grid_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]
    accessible_count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                adjacent_rolls = 0
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if grid[new_row][new_col] == '@':
                            adjacent_rolls += 1
                if adjacent_rolls < 4:
                    accessible_count += 1
    return accessible_count

def count_removable_rolls_iterative(grid_text):
    lines = grid_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    total_removed = 0
    iteration = 0
    while True:
        accessible_positions = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '@':
                    adjacent_rolls = 0
                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if grid[new_row][new_col] == '@':
                                adjacent_rolls += 1
                    if adjacent_rolls < 4:
                        accessible_positions.append((row, col))
        if not accessible_positions:
            break
        for row, col in accessible_positions:
            grid[row][col] = '.'
        iteration += 1
        total_removed += len(accessible_positions)
        print(f"Iteration {iteration}: Removed {len(accessible_positions)} rolls (total: {total_removed})")
    
    return total_removed

def paper_rolls(grid_text):
    accessible_once = count_accessible_rolls_once(grid_text)
    total_removable = count_removable_rolls_iterative(grid_text)
    return accessible_once, total_removable

grid = """
""".strip()

result_part1, result_part2 = paper_rolls(grid)
print(f"Iinitially accessible): {result_part1}")
print(f"Total removable): {result_part2}")