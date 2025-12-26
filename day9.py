# Day 9: Movie Theater

def find_largest_rectangle(input_text):
    red_tiles = set()
    for line in input_text.strip().split('\n'):
        if line.strip():
            x, y = map(int, line.split(','))
            red_tiles.add((x, y))
    tiles = list(red_tiles)
    n = len(tiles)
    max_area = 0
    best_rect = None
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            if x1 == x2 or y1 == y2:
                continue
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            if area > max_area:
                max_area = area
                best_rect = ((x1, y1), (x2, y2))    
    return max_area

red_tiles = """""".strip()

result = find_largest_rectangle(red_tiles)
print(f"Largest rectangle area: {result}")