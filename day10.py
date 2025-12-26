# Day 10: Factory

import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from itertools import product

def parse_machine(line):
    pattern_match = re.search(r'\[([.#]+)\]', line)
    if pattern_match:
        target_lights = [1 if c == '#' else 0 for c in pattern_match.group(1)]
    else:
        target_lights = None
    buttons = []
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    for button_str in button_matches:
        lights = [int(x.strip()) for x in button_str.split(',')]
        buttons.append(lights)
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    if joltage_match:
        target_joltage = [int(x.strip()) for x in joltage_match.group(1).split(',')]
    else:
        target_joltage = None
    return target_lights, target_joltage, buttons

def solve_lights_gf2(target, buttons): #Gaussian Elimination
    n_lights = len(target)
    n_buttons = len(buttons)
    matrix = []
    for light_i in range(n_lights): # Build augmented matrix [A | b]
        row = [0] * (n_buttons + 1)
        for btn_i, button in enumerate(buttons):
            if light_i in button:
                row[btn_i] = 1
        row[n_buttons] = target[light_i]
        matrix.append(row)
    pivot_cols = []
    current_row = 0
    
    for col in range(n_buttons):
        pivot_found = False
        for row in range(current_row, n_lights):
            if matrix[row][col] == 1:
                matrix[current_row], matrix[row] = matrix[row], matrix[current_row]
                pivot_found = True
                break
        if not pivot_found:
            continue
        pivot_cols.append(col)
        for row in range(n_lights):
            if row != current_row and matrix[row][col] == 1:
                for c in range(n_buttons + 1):
                    matrix[row][c] ^= matrix[current_row][c]
        current_row += 1
    for row in range(current_row, n_lights):
        if matrix[row][n_buttons] == 1:
            return None
    free_vars = [col for col in range(n_buttons) if col not in pivot_cols]
    min_presses = float('inf')
    
    for free_vals in product([0, 1], repeat=len(free_vars)):
        solution = [0] * n_buttons
        for i, var in enumerate(free_vars):
            solution[var] = free_vals[i]
        for row_i in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[row_i]
            val = matrix[row_i][n_buttons]
            for c in range(col + 1, n_buttons):
                val ^= (matrix[row_i][c] * solution[c])
            solution[col] = val
        presses = sum(solution)
        min_presses = min(min_presses, presses)
    return min_presses

def solve_joltage_milp(target, buttons, n_counters): #Minimisation
    n_buttons = len(buttons)
    A = np.zeros((n_counters, n_buttons), dtype=float)
    
    for btn_i, button in enumerate(buttons):
        for counter in button:
            if counter < n_counters:
                A[counter][btn_i] = 1.0
    
    b_lower = np.array(target, dtype=float)
    b_upper = np.array(target, dtype=float)
    c = np.ones(n_buttons)
    constraints = LinearConstraint(A, b_lower, b_upper)
    bounds = Bounds(lb=np.zeros(n_buttons), ub=np.inf)
    integrality = np.ones(n_buttons)
    
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    return int(np.sum(result.x))

def solve_all_machines(input_text):
    lines = input_text.strip().split('\n')

    total_lights = 0
    total_joltage = 0
    
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        target_lights, target_joltage, buttons = parse_machine(line)
        min_presses_lights = solve_lights_gf2(target_lights, buttons)
        total_lights += min_presses_lights
        
        min_presses_joltage = solve_joltage_milp(target_joltage, buttons, len(target_joltage))
        total_joltage += min_presses_joltage
    return total_lights, total_joltage

input_data = """"""

if input_data.strip():
    result_part1, result_part2 = solve_all_machines(input_data.strip())
    print(f"Indicator lights: {result_part1}")
    print(f"Joltage counters: {result_part2}")