from enum import StrEnum
from typing import List



def read_line_from_file():
    for line in open('input.txt'):
        yield line.rstrip('\n')

def read_muls_from_line(line: str):
    muls_instructions: List[str] = []
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
        muls_instructions.append(line[mul_index + 4: closing_per_index])
    return muls_instructions

def sum_multiplications(mul_instructions: List[str]):
    multiplications = []
    for mul_line in mul_instructions:
        try:
            first_num, second_num = mul_line.split(',')
            multiplications.append(int(first_num)*int(second_num))
        except ValueError:
            continue
    return sum(multiplications)

def solve_part_one():
    sum_of_muls = 0
    for line in read_line_from_file():
        sum_of_muls += sum_multiplications(read_muls_from_line(line))
    print(sum_of_muls)

solve_part_one()

def solve_part_two():
    class Instructions(StrEnum):
        do = "do()"
        dont = "don't()"
    sum_of_muls = 0
    last_instruction = Instructions.do
    for line in read_line_from_file():
        curr_index = 0
        next_do_index = 0
        while curr_index < len(line):
            if last_instruction == Instructions.dont:
                next_do_index = line.find(Instructions.do, curr_index)
            next_dont_index = line.find(Instructions.dont, next_do_index)
            if next_dont_index == -1:
                next_dont_index = len(line)
            last_instruction = Instructions.dont
            sum_of_muls += sum_multiplications(read_muls_from_line(line[next_do_index:next_dont_index]))
            curr_index = next_dont_index + 1
        last_instruction = Instructions.do if next_do_index != -1 else Instructions.dont
    print(sum_of_muls)

solve_part_two()