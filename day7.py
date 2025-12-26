# Day 7: Laboratories:

def count_splits(manifold_text):
    lines = manifold_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    start_col = -1
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    if start_col == -1:
        return 0
    beams = [(0, start_col)]
    activated_splitters = set()
    while beams:
        new_beams = []
        for row, col in beams:
            new_row = row + 1
            if new_row >= rows:
                continue
            cell = grid[new_row][col]
            if cell == '^':
                splitter_pos = (new_row, col)
                activated_splitters.add(splitter_pos)
                if col - 1 >= 0:
                    new_beams.append((new_row, col - 1))
                if col + 1 < cols:
                    new_beams.append((new_row, col + 1))
            elif cell in ['.', 'S']:
                new_beams.append((new_row, col))
        beams = new_beams
    return len(activated_splitters)

def count_paths(manifold_text):
    lines = manifold_text.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    start_col = -1
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    if start_col == -1:
        return 0
    memo = {} # Memoisation
    def count_paths_from(row, col):
        if row >= rows - 1:
            return 1
        if (row, col) in memo:
            return memo[(row, col)]
        next_row = row + 1
        if next_row >= rows:
            return 1
        cell = grid[next_row][col]
        total_paths = 0
        if cell == '^': #Split
            if col - 1 >= 0:
                total_paths += count_paths_from(next_row, col - 1)
            if col + 1 < cols:
                total_paths += count_paths_from(next_row, col + 1)
        elif cell in ['.', 'S']:
            total_paths += count_paths_from(next_row, col)
        memo[(row, col)] = total_paths
        return total_paths
    result = count_paths_from(0, start_col)
    return result

def solve_tachyon_manifold(manifold_text):
    splits = count_splits(manifold_text)
    paths = count_paths(manifold_text)
    return splits, paths

manifold = """""".strip()

result_part1, result_part2 = solve_tachyon_manifold(manifold)
print(f"Beam splits: {result_part1}")
print(f"Total paths: {result_part2}")