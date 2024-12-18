from collections import defaultdict


input = []

with open('input.txt', 'r') as fd:
    for line in fd.readlines():
        input.append(list(line.rstrip('\n')))

freq_points = defaultdict(list)

for j, row in enumerate(input):
    for i, cell in enumerate(row):
        if cell != '.':
            freq_points[cell].append((i, j))

def solve_part_one():
    antinode_points = set()
    for points in freq_points.values():
        for curr_point_i in range(len(points)):
            for pair_point_i in range(curr_point_i + 1, len(points)):
                curr_point = points[curr_point_i]
                pair_point = points[pair_point_i]
                dx = pair_point[0] - curr_point[0]
                dy = pair_point[1] - curr_point[1]

                antinode_1 = (curr_point[0] - dx, curr_point[1] - dy)
                if antinode_1[0] >= 0 and antinode_1[0] < len(input[0]) and antinode_1[1] >= 0 and antinode_1[1] < len(input):
                    antinode_points.add(antinode_1)
                antinode_2 = (pair_point[0] + dx, pair_point[1] + dy)
                if antinode_2[0] >= 0 and antinode_2[0] < len(input[0]) and antinode_2[1] >= 0 and antinode_2[1] < len(input):
                    antinode_points.add(antinode_2)
    print(len(antinode_points))


solve_part_one()


def solve_part_two():
    antinode_points = set()
    for points in freq_points.values():
        for curr_point_i in range(len(points)):
            for pair_point_i in range(curr_point_i + 1, len(points)):
                curr_point = points[curr_point_i]
                pair_point = points[pair_point_i]
                dx = pair_point[0] - curr_point[0]
                dy = pair_point[1] - curr_point[1]

                while curr_point[0] >= 0 and curr_point[0] < len(input[0]) and curr_point[1] >= 0 and curr_point[1] < len(input):
                    antinode_points.add(curr_point)
                    curr_point = (curr_point[0] + dx, curr_point[1] + dy)
                while pair_point[0] >= 0 and pair_point[0] < len(input[0]) and pair_point[1] >= 0 and pair_point[1] < len(input):
                    antinode_points.add(pair_point)
                    pair_point = (pair_point[0] - dx, pair_point[1] - dy)
    print(len(antinode_points))

solve_part_two()