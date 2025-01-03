from operator import xor

registers = {
    'A': 0,
    'B': 0,
    'C': 0
}

program = []

with open('input.txt', 'r') as fd:
    for line in fd.readlines():
        line = line.rstrip('\n')
        if ' A' in line:
            registers['A'] = int(line.split(' ')[-1])
        elif ' B' in line:
            registers['B'] = int(line.split(' ')[-1])
        elif ' C' in line:
            registers['C'] = int(line.split(' ')[-1])
        elif 'Program' in line:
            line = line.split(': ')[-1]
            [program.append(int(char)) for char in line.split(',')]

def combo(operand: int) -> int:
    if operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']
    return operand

printed = []

def adv(operand: int, register_to_store):
    registers[register_to_store] = registers['A'] // pow(2, combo(operand))

def run_op(opcode: int, operand: int, i: int) -> int:
    match opcode:
        case 0:
            adv(operand, 'A')
        case 1:
            registers['B'] ^= operand
        case 2:
            registers['B'] = combo(operand) % 8
        case 3:
            if registers['A']:
                return operand
        case 4:
            registers['B'] ^= registers['C']
        case 5:
            printed.append(str(combo(operand) % 8))
        case 6:
            adv(operand, 'B')
        case 7:
            adv(operand, 'C')
    return i + 2

def sovle_part_one():
    i = 0
    while i < len(program):
        i = run_op(program[i], program[i + 1], i)
    print(','.join(printed))

sovle_part_one()
