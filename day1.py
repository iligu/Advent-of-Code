# Day 1: Sectret Entrance

def solve_dial(instructions_text):
    dial = 50
    count_zeros_at_end = 0  
    count_zeros_any_click = 0 
    lines = instructions_text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        direction = line[0]
        amount = int(line[1:])
        
        if direction == 'L':
            for _ in range(amount):
                dial = (dial - 1) % 100
                if dial == 0:
                    count_zeros_any_click += 1
        elif direction == 'R':
            for _ in range(amount):
                dial = (dial + 1) % 100
                if dial == 0:
                    count_zeros_any_click += 1
        
        if dial == 0:
            count_zeros_at_end += 1
    
    return (count_zeros_any_click, count_zeros_at_end)

instructions = """"""

result_any_click, result_at_end = solve_dial(instructions)
print(f"Zeros during any click: {result_any_click}")
print(f"Zeros at end of rotation: {result_at_end}")