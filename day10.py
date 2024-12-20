from typing import List, Tuple


input = []

with open("input.txt") as file:
    for line in file:
        input.append([int(num) for num in list(line.rstrip('\n'))])

def calculate_trailhead_scores(j: int, i: int, next_step: int, trailheads: List[Tuple[int, int]]) -> int:
    if j < 0 or j >= len(input) or i < 0 or i >= len(input[j]):
        return 0
    if input[j][i] != next_step:
        return 0
    if input[j][i] == 9 and (j, i) not in trailheads:
        trailheads.append((j, i))
        return 1
    score = 0
    score += calculate_trailhead_scores(j+1, i, next_step+1, trailheads)
    score += calculate_trailhead_scores(j-1, i, next_step+1, trailheads)
    score += calculate_trailhead_scores(j, i+1, next_step+1, trailheads)
    score += calculate_trailhead_scores(j, i-1, next_step+1, trailheads)
    return score


def solve_part_one():
    sum_of_scores = 0
    for j in range(len(input)):
        for i in range(len(input[j])):
            if input[j][i] == 0:
                sum_of_scores += calculate_trailhead_scores(j, i, 0, [])
    print(sum_of_scores)

solve_part_one()


def calculate_unique_trail_scores(j: int, i: int, next_step: int) -> int:
    if j < 0 or j >= len(input) or i < 0 or i >= len(input[j]):
        return 0
    if input[j][i] != next_step:
        return 0
    if input[j][i] == 9:
        return 1
    score = 0
    score += calculate_unique_trail_scores(j+1, i, next_step+1)
    score += calculate_unique_trail_scores(j-1, i, next_step+1)
    score += calculate_unique_trail_scores(j, i+1, next_step+1)
    score += calculate_unique_trail_scores(j, i-1, next_step+1)
    return score

def solve_part_two():
    sum_of_scores = 0
    for j in range(len(input)):
        for i in range(len(input[j])):
            if input[j][i] == 0:
                sum_of_scores += calculate_unique_trail_scores(j, i, 0)
    print(sum_of_scores)

solve_part_two()