from enum import Enum
from typing import List, Tuple


maze: List[List[str]] = []

with open('input.txt', 'r') as fd:
    for line in fd:
        maze.append(list(line.rstrip('\n')))

class DIRECTION(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

turns = {
    DIRECTION.UP: [DIRECTION.RIGHT, DIRECTION.LEFT],
    DIRECTION.RIGHT: [DIRECTION.DOWN, DIRECTION.UP],
    DIRECTION.DOWN: [DIRECTION.LEFT, DIRECTION.RIGHT],
    DIRECTION.LEFT: [DIRECTION.UP, DIRECTION.DOWN]
}

next_move_deltas = {
    DIRECTION.UP: (0, -1),
    DIRECTION.DOWN: (0, 1),
    DIRECTION.LEFT: (-1, 0),
    DIRECTION.RIGHT: (1, 0)
}

def get_next_tile_coord(curr_x: int, curr_y: int, direction: DIRECTION) -> Tuple[int, int]:
    return tuple(map(sum, zip((curr_x, curr_y), next_move_deltas[direction])))

traceback_deltas = {
    DIRECTION.UP: (0, 1),
    DIRECTION.DOWN: (0, -1),
    DIRECTION.LEFT: (1, 0),
    DIRECTION.RIGHT: (-1, 0)
}

def get_traceback_tile_coord(curr_x: int, curr_y: int, direction: DIRECTION) -> Tuple[int, int]:
    return tuple(map(sum, zip((curr_x, curr_y), traceback_deltas[direction])))

def get_starting_position():
    for j in range(len(maze)):
        try:
            i = maze[j].index('S')
            return i, j
        except ValueError:
            pass

min_score = 1000000
maze_scores = [[89500 for _ in range(len(maze[0]))] for _ in range(len(maze))]

def rec_solve_maze(x: int, y: int, direction: DIRECTION, score: int):
    global min_score
    if maze[y][x] in ['#', 'X']:
        return
    if maze[y][x] == 'E':
        print(score)
        if score < min_score:
            min_score = score
        return
    if maze_scores[y][x] < score:
        return
    maze_scores[y][x] = score
    maze[y][x] = 'X'
    next_x, next_y = get_next_tile_coord(x, y, direction)
    # move forward while can
    while maze[next_y][next_x] == '.':
        maze_scores[next_y][next_x] = score
        maze[next_y][next_x] = 'X'
        next_x, next_y = get_next_tile_coord(next_x, next_y, direction)
        score += 1
    # if End, traverse back and remove Xs
    if maze[next_y][next_x] == 'E':
        print(score + 1)
        if score + 1 < min_score:
            min_score = score + 1
        next_x, next_y = get_traceback_tile_coord(next_x, next_y, direction)
        while x != next_x or y != next_y:
            maze[next_y][next_x] = '.'
            next_x, next_y = get_traceback_tile_coord(next_x, next_y, direction)
            score -= 1
        maze[next_y][next_x] = '.'
        return
    curr_x, curr_y = get_traceback_tile_coord(next_x, next_y, direction)
    while x != curr_x or y != curr_y:
        for turn in turns[direction]:
            next_x, next_y = get_next_tile_coord(curr_x, curr_y, turn)
            rec_solve_maze(next_x, next_y, turn, score + 1001)
        maze[curr_y][curr_x] = '.'
        curr_x, curr_y = get_traceback_tile_coord(curr_x, curr_y, direction)
        score -= 1
    for turn in turns[direction]:
        next_x, next_y = get_next_tile_coord(curr_x, curr_y, turn)
        rec_solve_maze(next_x, next_y, turn, score + 1001)
    maze[curr_y][curr_x] = '.'


def solve_part_one():
    x, y = get_starting_position()
    direction = DIRECTION.RIGHT
    rec_solve_maze(x, y, direction, 0)
    print(min_score)

solve_part_one()