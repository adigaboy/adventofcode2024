from copy import deepcopy
from enum import StrEnum, auto
from typing import Tuple


class Directions(StrEnum):
    up = '^'
    down = 'v'
    left = '<'
    right = '>'

lab_map = []

def read_input():
    with open('input.txt', 'r') as fd:
        for line in fd.readlines():
            lab_map.append(list(line.rstrip('\n')))

def find_mark_in_map() -> Tuple[int, int]:
    for j, line in enumerate(lab_map):
        if any(mark.value in line for mark in Directions):
            for mark in Directions:
                i = line.index(mark.value)
                if i != -1:
                    return j, i

def mark_if_not_passed(j: int, i: int) -> None:
    if lab_map[j][i] != 'X':
        lab_map[j][i] = 'X'
        return True
    return False

def get_next_direction(curr_direction: Directions) -> Directions:
    next_directions = {
        Directions.up: Directions.right,
        Directions.right: Directions.down,
        Directions.down: Directions.left,
        Directions.left: Directions.up
    }
    return next_directions[curr_direction]

def advance_while_you_can_and_count(j: int, i: int, direction: Directions) -> Tuple[int, int, int]:
    moves = 0
    if direction == Directions.up:
        while j > 0 and lab_map[j - 1][i] != '#':
            if mark_if_not_passed(j, i):
                moves += 1
            j -= 1
    if direction == Directions.down:
        while j < len(lab_map) - 1 and lab_map[j + 1][i] != '#':
            if mark_if_not_passed(j, i):
                moves += 1
            j += 1
    if direction == Directions.right:
        while i < len(lab_map) - 1 and lab_map[j][i + 1] != '#':
            if mark_if_not_passed(j, i):
                moves += 1
            i += 1
    if direction == Directions.left:
        while i > 0 and lab_map[j][i - 1] != '#':
            if mark_if_not_passed(j, i):
                moves += 1
            i -= 1
    return j, i, moves

def solve_part_one():
    count = 0
    read_input()
    curr_j, curr_i = find_mark_in_map()
    direction = lab_map[curr_j][curr_i]
    while curr_i not in [0, len(lab_map[0]) - 1] and curr_j not in [0, len(lab_map) - 1]:
        curr_j, curr_i, moves = advance_while_you_can_and_count(curr_j, curr_i, direction)
        count += moves
        if mark_if_not_passed(curr_j, curr_i):
            count += 1
        direction = get_next_direction(direction)
    print(count)

solve_part_one()


def check_if_looped(curr_j, curr_i) -> bool:
    direction = lab_map[curr_j][curr_i]
    while curr_i not in [0, len(lab_map[0]) - 1] and curr_j not in [0, len(lab_map) - 1]:
        curr_j, curr_i, moves = advance_while_you_can_and_count(curr_j, curr_i, direction)
        if not moves and not mark_if_not_passed(curr_j, curr_i):
            return True
        direction = get_next_direction(direction)
    return False

def solve_part_two():
    count = 0
    map_solved = deepcopy(lab_map)
    lab_map.clear()
    read_input()
    start_j, start_i = find_mark_in_map()
    for j in range(len(map_solved)):
        for i in range(len(map_solved[0])):
            if map_solved[j][i] == 'X' and (j != start_j or i != start_i):
                lab_map[j][i] = '#'
                if check_if_looped(start_j, start_i):
                    count += 1
                lab_map.clear()
                read_input()
    print(count)

solve_part_two()