# Day 3: Lobby

def find_max_joltage_2_digits(bank):
    digits = bank.strip()
    max_joltage = 0
    
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            two_digit = int(digits[i] + digits[j])
            max_joltage = max(max_joltage, two_digit)
    
    return max_joltage

def find_max_joltage_12_digits(bank):
    # Go Greedy – select the largest digit at each position while ensuring enough digits to complete 12
    digits = bank.strip()
    n = len(digits)
    
    if n < 12:
        return 0
    selected = []
    start = 0
    
    for position in range(12):
        remaining_needed = 12 - position - 1
        search_end = n - remaining_needed
        max_digit = '0'
        max_index = start
        
        for i in range(start, search_end):
            if digits[i] > max_digit:
                max_digit = digits[i]
                max_index = i
        
        selected.append(max_digit)
        start = max_index + 1
    
    return int(''.join(selected))

def calculate_total_joltage(banks):
    total_2_digits = 0
    total_12_digits = 0
    
    for bank in banks:
        if bank.strip():
            joltage_2 = find_max_joltage_2_digits(bank)
            joltage_12 = find_max_joltage_12_digits(bank)
            
            print(f"{bank.strip()[:30]}...: 2-digit={joltage_2}, 12-digit={joltage_12}")
            total_2_digits += joltage_2
            total_12_digits += joltage_12
    
    return total_2_digits, total_12_digits

banks = """""".strip().split('\n')

result_2_digits, result_12_digits = calculate_total_joltage(banks)
print(f"Total output joltage (2 digits): {result_2_digits}")
print(f"Total output joltage (12 digits): {result_12_digits}")