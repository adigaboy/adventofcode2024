
from enum import StrEnum, auto
from typing import List, Tuple


robot_map: List[List[str]] = []
moves: List[str] = []

with open('input.txt', 'r') as fd:
    line = fd.readline()
    while line != '\n':
        robot_map.append(list(line.rstrip('\n')))
        line = fd.readline()

    for line in fd.readlines():
        moves.extend(list(line.rstrip('\n')))

def find_initial_position() -> Tuple[int, int]:
    for j, row in enumerate(robot_map):
        try:
            i = row.index('@')
            return i, j
        except ValueError:
            continue

class MOVES(StrEnum):
    up = '^'
    down = 'v'
    left = '<'
    right = '>'

next_move_deltas = {
    MOVES.up: (0, -1),
    MOVES.down: (0, 1),
    MOVES.left: (-1, 0),
    MOVES.right: (1, 0)
}

traceback_deltas = {
    MOVES.up: (0, 1),
    MOVES.down: (0, -1),
    MOVES.left: (1, 0),
    MOVES.right: (-1, 0)
}


def move_robot(x: int, y: int, direction: MOVES) -> Tuple[int, int]:
    next_x, next_y = tuple(map(sum, zip((x, y), next_move_deltas[direction])))
    if robot_map[next_y][next_x] == '#':
        return (x, y)
    if robot_map[next_y][next_x] == 'O':
        curr_x, curr_y = next_x, next_y
        while robot_map[curr_y][curr_x] == 'O':
            curr_x, curr_y = tuple(map(sum, zip((curr_x, curr_y), next_move_deltas[direction])))
        if robot_map[curr_y][curr_x] == '#':
            return (x, y)
        next_x, next_y = curr_x, curr_y
    while next_x != x or next_y != y:
        curr_x, curr_y = next_x, next_y
        next_x, next_y = tuple(map(sum, zip((curr_x, curr_y), traceback_deltas[direction])))
        robot_map[curr_y][curr_x] = robot_map[next_y][next_x]
    robot_map[curr_y][curr_x] = '.'
    return tuple(map(sum, zip((x, y), next_move_deltas[direction])))

def sum_boxes_coordinates():
    boxes_sum = 0
    for j, row in enumerate(robot_map):
        for i, space in enumerate(row):
            if space == 'O':
                boxes_sum += (100 * j) + i
    return boxes_sum

def solve_part_one():
    curr_x, curr_y = find_initial_position()
    for move in moves:
        curr_x, curr_y = move_robot(curr_x, curr_y, move)
    print(sum_boxes_coordinates())

solve_part_one()
