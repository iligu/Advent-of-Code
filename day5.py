# Day 5: Cafeteria

def check_available_fresh(input_text):
    sections = input_text.strip().split('\n\n')    
    ranges_text = sections[0].strip().split('\n')
    fresh_ranges = []
    for range_str in ranges_text:
        start, end = map(int, range_str.split('-'))
        fresh_ranges.append((start, end))
    available_ids = [int(id_str.strip()) for id_str in sections[1].strip().split('\n')]
    fresh_count = 0
    
    for ingredient_id in available_ids:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1    
    return fresh_count

def count_total_fresh_ids(input_text):
    sections = input_text.strip().split('\n\n')
    ranges_text = sections[0].strip().split('\n')
    ranges = []
    for range_str in ranges_text:
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    ranges.sort()
    merged_ranges = []
    for start, end in ranges:
        if not merged_ranges:
            merged_ranges.append((start, end))
        else:
            last_start, last_end = merged_ranges[-1]
            if start <= last_end + 1:
                merged_ranges[-1] = (last_start, max(last_end, end))
            else:
                merged_ranges.append((start, end))
    total_fresh = 0
    for start, end in merged_ranges:
        count = end - start + 1
        total_fresh += count
    
    return total_fresh

def solve_ingredient_freshness(input_text):
    available_fresh = check_available_fresh(input_text)
    total_fresh = count_total_fresh_ids(input_text)
    
    return available_fresh, total_fresh

input_data = """""".strip()

result_part1, result_part2 = solve_ingredient_freshness(input_data)
print(f"Available ingredients that are fresh): {result_part1}")
print(f"Ttotal fresh IDs covered by ranges): {result_part2}")