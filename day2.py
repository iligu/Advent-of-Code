# Day 2: Gift Shop

def is_invalid_id_twice(num):
    s = str(num)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

def is_invalid_id_atleast_twice(num):
    s = str(num)
    length = len(s)
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repeats = length // pattern_len
            if pattern * repeats == s and repeats >= 2:
                return True
    return False

def find_invalid_ids(ranges):
    total_atleast_twice = 0
    total_exactly_twice = 0
    
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        
        for num in range(start, end + 1):
            if is_invalid_id_atleast_twice(num):
                total_atleast_twice += num
            if is_invalid_id_twice(num):
                total_exactly_twice += num
    
    return total_atleast_twice, total_exactly_twice

ranges = """
"""

ranges = [r.strip() for r in ranges.strip().split('\n') if r.strip()]

result_atleast, result_exactly = find_invalid_ids(ranges)
print(f"Sum of invalid IDs (at least twice): {result_atleast}")
print(f"Sum of invalid IDs (exactly twice): {result_exactly}")