
from collections import defaultdict
from typing import List


order_of_app = defaultdict(list)
page_updates: List[List[int]] = []

with open('input.txt', 'r') as fd:
    line = fd.readline().rstrip('\n')
    while line != '':
        numA, numB = line.split('|')
        order_of_app[int(numB)].append(int(numA))
        line = fd.readline().rstrip('\n')
    for line in fd.readlines():
        line.rstrip('\n')
        page_updates.append([int(num) for num in line.split(',')])

def is_order_correct(updates: List[int]) -> bool:
    for i, page_num in enumerate(updates):
        if any(page in order_of_app[page_num] for page in updates[i+1:]):
            return False
    return True

def solve_part_one():
    sum_of_mids = 0
    for updates in page_updates:
        if is_order_correct(updates):
            sum_of_mids += updates[int(len(updates) / 2)]
    print(sum_of_mids)

solve_part_one()

def solve_part_two():
    sum_of_mids = 0
    for updates in page_updates:
        if not is_order_correct(updates):
            # bubble sort
            for i in range(len(updates) - 1):
                for j in range(len(updates) - i - 1):
                    if updates[j + 1] in order_of_app[updates[j]]:
                        tmp = updates[j + 1]
                        updates[j + 1] = updates[j]
                        updates[j] = tmp
            sum_of_mids += updates[int(len(updates) / 2)]
    print(sum_of_mids)

solve_part_two()
