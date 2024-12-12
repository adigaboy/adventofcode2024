from typing import List


muls_int_text: List[str] = []

def read_muls_from_line(line: str):
    curr_index = 0
    while curr_index < len(line):
        mul_index = line.find('mul(', curr_index)
        if mul_index == -1:
            break
        closing_per_index = line.find(')', mul_index + 1)
        next_mul_index = line.find('mul(', mul_index + 1)
        if next_mul_index != -1 and closing_per_index > next_mul_index:
            curr_index = next_mul_index
            continue
        curr_index = closing_per_index + 1
        muls_int_text.append(line[mul_index + 4: closing_per_index])

def read_all_mul_instructions_from_input():
    with open('input.txt', 'r') as fd:
        for line in fd.readlines():
            line = line.rstrip('\n')
            read_muls_from_line(line)

def sum_multiplications():
    multiplications = []
    for mul_line in muls_int_text:
        try:
            first_num, second_num = mul_line.split(',')
            multiplications.append(int(first_num)*int(second_num))
        except ValueError:
            continue
    return sum(multiplications)

def solve_part_one():
    read_all_mul_instructions_from_input()
    print(sum_multiplications())

solve_part_one()

muls_int_text: List[str] = []

def read_do_mul_instructions_from_input():
    full_input = None
    with open('input.txt', 'r') as fd:
        full_input = ''.join(fd.readlines())
    first_dont_index = full_input.find("don't()")
    read_muls_from_line(full_input[:first_dont_index])
    curr_index = first_dont_index + 1
    while curr_index < len(full_input):
        next_do_index = full_input.find("do()", curr_index)
        next_dont_index = full_input.find("don't()", next_do_index)
        if next_dont_index == -1:
            next_dont_index = len(full_input)
        read_muls_from_line(full_input[next_do_index:next_dont_index])
        curr_index = next_dont_index + 1

def solve_part_two():
    read_do_mul_instructions_from_input()
    print(sum_multiplications())

solve_part_two()