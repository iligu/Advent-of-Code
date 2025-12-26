# Day 12: Christmas Tree Farm
import time

def parse_input(input_text):
    lines = input_text.strip().split('\n')
    shapes = {}
    regions = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and ':' in line and line.split(':')[0].strip().isdigit():
            shape_id = int(line.split(':')[0].strip())
            shape_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() and ':' not in lines[i]:
                shape_lines.append(lines[i])
                i += 1
            if shape_lines:
                shapes[shape_id] = parse_shape(shape_lines)
            continue
        elif line and 'x' in line and ':' in line:
            parts = line.split(':')
            dims = parts[0].strip().split('x')
            width, height = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].strip().split()))
            regions.append((width, height, counts))
        i += 1
    return shapes, regions

def parse_shape(lines):
    coords = set()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '#':
                coords.add((r, c))
    return coords

def get_rotations_and_flips(shape):
    orientations = []
    for flip in [False, True]:
        current = shape.copy()
        if flip and current:
            max_c = max(c for r, c in current)
            current = {(r, max_c - c) for r, c in current}
        for _ in range(4):
            if current:
                min_r = min(r for r, c in current)
                min_c = min(c for r, c in current)
                normalized = frozenset((r - min_r, c - min_c) for r, c in current)
                if normalized not in [frozenset(o) for o in orientations]:
                    orientations.append(set(normalized))
            current = {(c, -r) for r, c in current}
    return orientations

def can_place(grid, shape, start_r, start_c, width, height):
    for dr, dc in shape:
        r, c = start_r + dr, start_c + dc
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        if grid[r][c] != '.':
            return False
    return True

def place_shape(grid, shape, start_r, start_c, label):
    """Place shape on grid"""
    for dr, dc in shape:
        r, c = start_r + dr, start_c + dc
        grid[r][c] = label

def remove_shape(grid, shape, start_r, start_c):
    """Remove shape from grid"""
    for dr, dc in shape:
        r, c = start_r + dr, start_c + dc
        grid[r][c] = '.'

def count_empty_cells(grid):
    """Count empty cells in grid"""
    return sum(1 for row in grid for cell in row if cell == '.')

def solve_packing(width, height, shapes_list, timeout=10):
    """Try to pack all shapes into the region using backtracking with pruning"""
    grid = [['.' for _ in range(width)] for _ in range(height)]
    start_time = time.time()
    
    # Early check: do shapes fit by area?
    total_shape_area = sum(len(orientations[0]) for _, orientations in shapes_list)
    grid_area = width * height
    if total_shape_area > grid_area:
        return False
    
    def backtrack(shape_idx):
        # Timeout check
        if time.time() - start_time > timeout:
            return None  # Timeout
        
        if shape_idx >= len(shapes_list):
            return True  # All shapes placed
        
        shape_id, orientations = shapes_list[shape_idx]
        
        # Pruning: check if remaining shapes can fit in remaining space
        remaining_area = sum(len(shapes_list[i][1][0]) for i in range(shape_idx, len(shapes_list)))
        empty_cells = count_empty_cells(grid)
        if remaining_area > empty_cells:
            return False
        
        # Try all positions and orientations
        for r in range(height):
            for c in range(width):
                # Skip if this position is already occupied
                if grid[r][c] != '.':
                    continue
                
                for orientation in orientations:
                    if can_place(grid, orientation, r, c, width, height):
                        place_shape(grid, orientation, r, c, chr(65 + shape_idx))
                        
                        result = backtrack(shape_idx + 1)
                        if result is True:
                            return True
                        elif result is None:
                            return None  # Propagate timeout
                        
                        remove_shape(grid, orientation, r, c)
        
        return False
    
    result = backtrack(0)
    return result if result is not None else False

def solve_regions(input_text):
    """Determine how many regions can fit their presents"""
    shapes, regions = parse_input(input_text)
    
    print(f"Found {len(shapes)} shapes")
    print(f"Found {len(regions)} regions to check\n")
    
    fittable_count = 0
    
    for idx, (width, height, counts) in enumerate(regions, 1):
        print(f"Region {idx}: {width}x{height}")
        print(f"  Required counts: {counts}")
        
        # Build list of shapes to place
        shapes_list = []
        for shape_id, count in enumerate(counts):
            if count > 0 and shape_id in shapes:
                for _ in range(count):
                    orientations = get_rotations_and_flips(shapes[shape_id])
                    shapes_list.append((shape_id, orientations))
        
        print(f"  Total presents to place: {len(shapes_list)}")
        
        # Try to pack with timeout
        can_fit = solve_packing(width, height, shapes_list, timeout=10)
        
        if can_fit:
            print(f"  ✓ CAN FIT")
            fittable_count += 1
        else:
            print(f"  ✗ CANNOT FIT")
        print()
    
    return fittable_count
input = """"""

if input.strip():
    print("=" * 50)
    print("YOUR INPUT:")
    result = solve_regions(input.strip())
    print(f"\nRegions that can fit all presents: {result}")