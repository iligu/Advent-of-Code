# Day 11: Reactor

from collections import defaultdict

def parse_connections(input_text):
    graph = defaultdict(list)
    for line in input_text.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split(':')
        if len(parts) != 2:
            continue
        device = parts[0].strip()
        outputs = parts[1].strip().split()
        graph[device] = outputs
    return graph

def count_all_paths(graph, start='you', end='out'):
    memo = {}
    def count_from(node):
        if node == end:
            return 1
        if node in memo:
            return memo[node]
        if node not in graph:
            return 0
        total = 0
        for neighbor in graph[node]:
            total += count_from(neighbor)
        memo[node] = total
        return total
    return count_from(start)

def count_paths_with_required(graph, start='svr', end='out', required={'dac', 'fft'}):
    memo = {}
    def count_from(node, visited_required):
        if node == end:
            return 1 if visited_required == required else 0
        state = (node, frozenset(visited_required))
        if state in memo:
            return memo[state]
        if node not in graph:
            memo[state] = 0
            return 0
        total = 0
        for neighbor in graph[node]:
            new_visited = visited_required.copy()
            if neighbor in required:
                new_visited.add(neighbor)
            total += count_from(neighbor, new_visited)
        
        memo[state] = total
        return total
    initial = set()
    if start in required:
        initial.add(start)
    
    return count_from(start, initial)

def solve_device_paths(input_text):
    graph = parse_connections(input_text)
    result_part1 = count_all_paths(graph, start='you', end='out')
    result_part2 = count_paths_with_required(graph, start='svr', end='out', required={'dac', 'fft'})
    return result_part1, result_part2

input = """"""

result_part1, result_part2 = solve_device_paths(input.strip())
print(f"All paths: {result_part1}")
print(f"Paths svr→out via dac+fft: {result_part2}")