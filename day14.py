
from time import sleep
from typing import List


class Robot:
    def __init__(self, x: int, y: int, x_vel: int, y_vel: int):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
    
    def move(self, seconds: int = 1):
        self.x += self.x_vel * seconds
        self.x %= 101
        if self.x < 0:
            self.x += 101
        self.y += self.y_vel * seconds
        self.y %= 103
        if self.y < 0:
            self.y += 103

robots: List[Robot] = []

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        p, v = line.split(' ')
        x, y = p[2:].split(',')
        x_vel, y_vel = v[2:].split(',')
        robots.append(Robot(int(x), int(y), int(x_vel), int(y_vel)))

def solve_part_one():
    for robot in robots:
        robot.move(100)
    quads = [0, 0, 0, 0]
    for robot in robots:
        if robot.x < 50 and robot.y < 51:
            quads[0] += 1
        elif robot.x > 50 and robot.y < 51:
            quads[1] += 1
        elif robot.x < 50 and robot.y > 51:
            quads[2] += 1
        elif robot.x > 50 and robot.y > 51:
            quads[3] += 1
    print(quads[0] * quads[1] * quads[2] * quads[3])
# solve_part_one()

def solve_part_two():
    with open('output.txt', '+w') as fd:
        for i in range(10000):
            for robot in robots:
                robot.move(1)
            drawing = [['.' for _ in range(101)] for __ in range(103)]
            for robot in robots:
                drawing[robot.y][robot.x] = '#'
            for row in drawing:
                if ''.join(row).find('##########') != -1:
                    return i

print(solve_part_two())