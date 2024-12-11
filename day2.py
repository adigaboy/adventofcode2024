
from typing import List


reports = []

with open('input.txt', 'r') as fd:
    for line in fd.readlines():
        reports.append([int(num) for num in line.rstrip('\n').split(' ')])


def check_report(report: List[int]) -> bool:
    is_ascending = report[1] > report[0]
    prev_level = report[0]
    for curr_level in report[1:]:
        dt = curr_level - prev_level
        if dt < 0 and is_ascending or dt > 0 and not is_ascending or dt not in [-3, -2, -1, 1, 2, 3]:
            return False
        prev_level = curr_level
    return True

def solve_part_one():
    safe_reports = 0
    for report in reports:
        if check_report(report):
            safe_reports += 1
    return safe_reports

print(solve_part_one())

def solve_part_two():
    safe_reports = 0
    for report in reports:
        if check_report(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                if check_report(report[: i] + report[i + 1:]):
                    safe_reports += 1
                    break
    return safe_reports

print(solve_part_two())