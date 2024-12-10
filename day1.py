
left_input = []
right_input = []

with open('input.txt', 'r') as fd:
    for line in fd.readlines():
        left_num, right_num = line.split('  ')
        left_input.append(int(left_num))
        right_input.append(int(right_num))

def solve_part_one():
    total_distance = 0
    for left_distance, right_distance in zip(sorted(left_input), sorted(right_input)):
        total_distance += abs(left_distance - right_distance)
    return total_distance

def solve_part_two():
    left_input_unique_counts = {}
    right_input_unique_counts = {}
    for num in set(left_input):
        left_input_unique_counts[num] = left_input.count(num)
    for num in set(right_input):
        right_input_unique_counts[num] = right_input.count(num)

    similarities = 0
    for left_num, occurrence in left_input_unique_counts.items():
        similarities += left_num * occurrence * right_input_unique_counts.get(left_num, 0)
    return similarities

print(solve_part_one())
print(solve_part_two())