
from functools import reduce
import itertools
from operator import mul
from typing import List


input = []

with open('input.txt', 'r') as fd:
    for line in fd.readlines():
        result, equation = line.rstrip('\n').split(': ')
        input.append({
            'result': int(result),
            'numbers': [int(num) for num in equation.split(' ')]
        })

known_options = {}

def generate_options(n) -> List[str]:
    if n in known_options:
        return known_options[n]
    options = list(itertools.product(['+', '*'], repeat=n))
    known_options[n] = options
    return options

def solve_part_one():
    sum_of_results = 0
    for equation in input:
        target_result = equation['result']
        numbers = equation['numbers']
        operations_options = generate_options(len(numbers) - 1)
        for option in operations_options:
            cal_result = numbers[0]
            for i, operator in enumerate(option):
                if operator == '+':
                    cal_result += numbers[i + 1]
                else:
                    cal_result *= numbers[i + 1]
                if cal_result > target_result:
                    break
            else:
                if cal_result == target_result:
                    sum_of_results += target_result
                    break
    print(sum_of_results)

solve_part_one()