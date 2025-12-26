# Day 8: Playground

import math

def solve_junction_boxes_part1(input_text, num_connections=1000):
    boxes = []
    for line in input_text.strip().split('\n'):
        if line.strip():
            x, y, z = map(int, line.split(','))
            boxes.append((x, y, z))
    n = len(boxes)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = boxes[i][0] - boxes[j][0]
            dy = boxes[i][1] - boxes[j][1]
            dz = boxes[i][2] - boxes[j][2]
            dist = math.sqrt(dx*dx + dy*dy + dz*dz)
            distances.append((dist, i, j))
    distances.sort()
    parent = list(range(n))
    size = [1] * n
    
    def find(x): #UFDS
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
        return True
    connections_made = 0
    for dist, i, j in distances:
        if connections_made >= num_connections:
            break
        if union(i, j):
            connections_made += 1
    component_sizes = {}
    for i in range(n):
        root = find(i)
        component_sizes[root] = component_sizes.get(root, 0) + 1
    sizes = sorted(component_sizes.values(), reverse=True)
    
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
        return result

def solve_junction_boxes_part2(input_text):    
    boxes = []
    for line in input_text.strip().split('\n'):
        if line.strip():
            x, y, z = map(int, line.split(','))
            boxes.append((x, y, z))
    n = len(boxes)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = boxes[i][0] - boxes[j][0]
            dy = boxes[i][1] - boxes[j][1]
            dz = boxes[i][2] - boxes[j][2]
            dist = math.sqrt(dx*dx + dy*dy + dz*dz)
            distances.append((dist, i, j))
    distances.sort()
    parent = list(range(n))
    size = [1] * n
    num_components = n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
        return True
    
    for dist, i, j in distances:
        if union(i, j):
            num_components -= 1
            if num_components == 1:
                x1, x2 = boxes[i][0], boxes[j][0]
                result = x1 * x2
                return result

def solve_junction_boxes(input_text, num_connections=1000):    
    result_part1 = solve_junction_boxes_part1(input_text, num_connections)
    result_part2 = solve_junction_boxes_part2(input_text)
    return result_part1, result_part2

junction_boxes = """""".strip()

result_part1, result_part2 = solve_junction_boxes(junction_boxes, num_connections=1000)
print(f"Product of 3 largest circuits after 1000 connections: {result_part1}")
print(f"Product of X coordinates of last connection: {result_part2}")