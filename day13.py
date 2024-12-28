
machines = []
def read_inpue():
    with open('input.txt') as f:
        for line in f:
            if 'Button A' in line:
                machines.append({
                    'A': {
                        'x': int(line[line.index('X+')+2:line.index(', Y')]),
                        'y': int(line[line.index('Y+')+2:])
                    }
                })
            elif 'Button B' in line:
                machines[-1]['B'] = {
                    'x': int(line[line.index('X+')+2:line.index(', Y')]),
                    'y': int(line[line.index('Y+')+2:])
                }
            elif 'Prize' in line:
                machines[-1]['prize'] = {
                    'x': int(line[line.index('X=')+2:line.index(', Y')]),
                    'y': int(line[line.index('Y=')+2:])
                }

read_inpue()

def solve_two_equations_with_two_variables(x1, x2, x_target, y1, y2, y_target):
    B = (x_target * y1 - y_target * x1) / (x2 * y1 - x1 * y2)
    if B != int(B):
        return None, None
    A = (x_target - B * x2) / x1
    if A != int(A):
        return None, None
    return (int(A), int(B))

def solve_part_one():
    result = 0
    for machine in machines:
        x_target = machine['prize']['x']
        y_target = machine['prize']['y']
        A, B = solve_two_equations_with_two_variables(machine['A']['x'], machine['B']['x'], x_target, machine['A']['y'], machine['B']['y'], y_target)
        if A and B is not None:
            result += A * 3 + B
    print(result)

solve_part_one()

def solve_part_two():
    result = 0
    for machine in machines:
        x_target = machine['prize']['x'] + 10000000000000
        y_target = machine['prize']['y'] + 10000000000000
        A, B = solve_two_equations_with_two_variables(machine['A']['x'], machine['B']['x'], x_target, machine['A']['y'], machine['B']['y'], y_target)
        if A and B is not None:
            result += A * 3 + B
    print(result)

solve_part_two()
