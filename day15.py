
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

def find_initial_position(current_map) -> Tuple[int, int]:
    for j, row in enumerate(current_map):
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


def get_next_tile_coord(curr_x: int, curr_y: int, direction: MOVES) -> Tuple[int, int]:
    return tuple(map(sum, zip((curr_x, curr_y), next_move_deltas[direction])))

def get_traceback_tile_coord(curr_x: int, curr_y: int, direction: MOVES) -> Tuple[int, int]:
    return tuple(map(sum, zip((curr_x, curr_y), traceback_deltas[direction])))

def move_robot(x: int, y: int, direction: MOVES) -> Tuple[int, int]:
    next_x, next_y = get_next_tile_coord(x, y, direction)
    curr_x, curr_y = next_x, next_y
    while robot_map[curr_y][curr_x] == 'O':
        curr_x, curr_y = get_next_tile_coord(curr_x, curr_y, direction)
    if robot_map[curr_y][curr_x] == '#':
        return x, y
    while curr_x != x or curr_y != y:
        prev_x, prev_y = curr_x, curr_y
        curr_x, curr_y = get_traceback_tile_coord(curr_x, curr_y, direction)
        robot_map[prev_y][prev_x] = robot_map[next_y][next_x]
    robot_map[curr_y][curr_x] = '.'
    return next_x, next_y

def sum_boxes_coordinates():
    boxes_sum = 0
    for j, row in enumerate(robot_map):
        for i, space in enumerate(row):
            if space == 'O':
                boxes_sum += (100 * j) + i
    return boxes_sum

def solve_part_one():
    curr_x, curr_y = find_initial_position(robot_map)
    for move in moves:
        curr_x, curr_y = move_robot(curr_x, curr_y, move)
    print(sum_boxes_coordinates())

scaled_map = []

def scale_up_map():
    for j, row in enumerate(robot_map):
        scaled_map.append([])
        for tile in row:
            if tile == '#':
                scaled_map[j].extend(['#', '#'])
            elif tile == 'O':
                scaled_map[j].extend(['[', ']'])
            elif tile == '.':
                scaled_map[j].extend(['.', '.'])
            elif tile == '@':
                scaled_map[j].extend(['@', '.'])

scale_up_map()
solve_part_one()


def rec_push_boxes(x: int, y: int, direction: MOVES):
    if scaled_map[y][x] == '.':
        return True
    next_x, next_y = get_next_tile_coord(x, y, direction)
    if rec_push_boxes(next_x, next_y, direction):
        if direction in [MOVES.up, MOVES.down]:
            if scaled_map[y][x] == '[':
                if rec_push_boxes(next_x + 1, next_y, direction):
                    scaled_map[next_y][next_x + 1] = scaled_map[y][x + 1]
                    scaled_map[y][x + 1] = '.'
            else:
                if rec_push_boxes(next_x - 1, next_y, direction):
                    scaled_map[next_y][next_x - 1] = scaled_map[y][x - 1]
                    scaled_map[y][x - 1] = '.'
        scaled_map[next_y][next_x] = scaled_map[y][x]
        scaled_map[y][x] = '.'
    return True


def rec_check_boxes(x: int, y: int, direction: MOVES) -> bool:
    if scaled_map[y][x] == '#':
        return False
    if scaled_map[y][x] == '.':
        return True
    next_x, next_y = get_next_tile_coord(x, y, direction)
    res = rec_check_boxes(next_x, next_y, direction)
    if not res:
        return False
    if direction in [MOVES.down, MOVES.up]:
        if scaled_map[y][x] == '[':
            res = rec_check_boxes(next_x + 1, next_y, direction)
            if not res:
                return False
        else:
            res = rec_check_boxes(next_x - 1, next_y, direction)
            if not res:
                return False
    return True

def check_if_can_push_boxes(x: int, y: int, direction: MOVES) -> bool:
    return rec_check_boxes(x, y, direction)

def push_boxes(x: int, y: int, direction: MOVES) -> bool:
    next_x, next_y = get_next_tile_coord(x, y, direction)
    if check_if_can_push_boxes(next_x, next_y, direction):
        rec_push_boxes(next_x, next_y, direction)
        return True
    return False

def move_robot_scaled(x: int, y: int, direction: MOVES) -> Tuple[int, int]:
    next_x, next_y = get_next_tile_coord(x, y, direction)
    pushed = False
    if scaled_map[next_y][next_x] == '#':
        return x, y
    elif scaled_map[next_y][next_x] != '.':
        pushed = push_boxes(x, y, direction)
    if pushed or scaled_map[next_y][next_x] == '.':
        scaled_map[next_y][next_x] = '@'
        scaled_map[y][x] = '.'
        return next_x, next_y
    return x, y


def sum_scaled_boxes_coordinates():
    boxes_sum = 0
    for j, row in enumerate(scaled_map):
        for i, space in enumerate(row):
            if space == '[':
                boxes_sum += (100 * j) + i
    return boxes_sum


def solve_part_two():
    curr_x, curr_y = find_initial_position(scaled_map)
    for move in moves:
        curr_x, curr_y = move_robot_scaled(curr_x, curr_y, move)
    print(sum_scaled_boxes_coordinates())

solve_part_two()