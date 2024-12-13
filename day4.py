XMAS = 'XMAS'

input = []

with open('input.txt', 'r') as fd:
    for line in fd.readlines():
        input.append(line.rstrip('\n'))


def solve_part_one():
    count = 0
    for j in range(len(input)):
        for i in range(len(input[j])):
            if input[j][i] != 'X':
                continue
            if  i < len(input[j]) - 3:
                # check right #
                if input[j][i:i+4] == XMAS:
                    count += 1
                # check up right #
                if j > 2 and ''.join([input[j-k][i+k] for k in range(4)]) == XMAS:
                    count += 1
                # check down right #
                if j < len(input) - 3 and ''.join([input[j+k][i+k] for k in range(4)]) == XMAS:
                    count += 1
            if i > 2:
                # check left #
                if ''.join([input[j][i-k] for k in range(4)]) == XMAS:
                    count += 1
                # check up left #
                if j > 2 and ''.join([input[j-k][i-k] for k in range(4)]) == XMAS:
                    count += 1
                # check down left #
                if j < len(input) - 3 and ''.join([input[j+k][i-k] for k in range(4)]) == XMAS:
                    count += 1
            # check up #
            if j > 2 and ''.join([input[j-k][i] for k in range(4)]) == XMAS:
                count += 1
            # check down #
            if j < len(input) - 3 and ''.join([input[j+k][i] for k in range(4)]) == XMAS:
                count += 1
    print(count)
solve_part_one()

SAMMAS = ["SAM", "MAS"]

def solve_part_two():
    count = 0
    for j in range(1, len(input) - 1):
        for i in range(1, len(input[j]) - 1):
            if input[j][i] != 'A':
                continue
            num_of_mas = 0
            if ''.join([input[j-1][i-1], input[j][i], input[j+1][i+1]]) in SAMMAS:
                num_of_mas += 1
            if ''.join([input[j+1][i-1], input[j][i], input[j-1][i+1]]) in SAMMAS:
                num_of_mas += 1
            if num_of_mas == 2:
                count += 1
    print(count)

solve_part_two()