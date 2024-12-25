from collections import defaultdict
from typing import Dict, List, Tuple


input = []

with open('input.txt', 'r') as fd:
    for line in fd:
        input.append(line.rstrip('\n'))

def rec_get_regions(j: int, i: int, plots: List[Tuple[int, int]], region: List[int]):
    if j < 0 or j >= len(input) or i < 0 or i >= len(input[0]):
        return
    if (i, j) not in plots:
        return
    region.append((i, j))
    plots[plots.index((i, j))] = (-1, -1)
    rec_get_regions(j - 1, i, plots, region)
    rec_get_regions(j + 1, i, plots, region)
    rec_get_regions(j, i - 1, plots, region)
    rec_get_regions(j, i + 1, plots, region)

def sperate_to_regions(plants: List[Tuple[int, int]]) -> Dict[str, List[Tuple[int, int]]]:
    result = {}
    for plant, plots in plants.items():
        regions = []
        for plot in plots:
            if plot != (-1, -1):
                region = []
                rec_get_regions(plot[1], plot[0], plots, region)
                regions.append(region)
        result[plant] = regions
    return result

def caclulate_fence_price(regions: List[Tuple[int, int]]) -> int:
    result = 0
    for region in regions:
        region_parimeter = 0
        for plot in region:
            parimeters = 0
            if plot[0] == 0 or (plot[0] - 1, plot[1]) not in region:
                parimeters += 1
            if plot[0] + 1 == len(input[0]) or (plot[0] + 1, plot[1]) not in region:
                parimeters += 1
            if plot[1] == 0 or (plot[0], plot[1] - 1) not in region:
                parimeters += 1
            if plot[1] + 1 == len(input[0]) or (plot[0], plot[1] + 1) not in region:
                parimeters += 1
            region_parimeter += parimeters
        result += region_parimeter * len(region)
    return result

def solve_part_one():
    plants = defaultdict(list)
    for j, row in enumerate(input):
        for i, plant in enumerate(row):
            plants[plant].append((i, j))

    plants = sperate_to_regions(plants)
    total_fence_price = 0
    for plant, regions in plants.items():
        total_fence_price += caclulate_fence_price(regions)
    print(total_fence_price)

solve_part_one()

def calcualate_discount_price(regions: List[Tuple[int, int]]) -> int:
    result = 0
    # check side on x axis:
    for region in regions:
        sides = 0
        for j in set(plot[1] for plot in region):
            plots_on_j = [p for p in region if p[1] == j]
            plots_on_j.sort(key=lambda x: x[0])
            prev_x = plots_on_j[0][0]
            is_top_same_side = False
            is_bottom_same_side = False
            for curr_plot in plots_on_j:
                if (curr_plot[0], j - 1) not in region:
                    if curr_plot[0] - 1 != prev_x:
                        is_top_same_side = False
                    if not is_top_same_side:
                        sides += 1
                    is_top_same_side = True
                else:
                    is_top_same_side = False
                if (curr_plot[0], j + 1) not in region:
                    if curr_plot[0] - 1 != prev_x:
                        is_bottom_same_side = False
                    if not is_bottom_same_side:
                        sides += 1
                    is_bottom_same_side = True
                else:
                    is_bottom_same_side = False
                prev_x = curr_plot[0]
        for i in set(plot[0] for plot in region):
            plots_on_i = [p for p in region if p[0] == i]
            plots_on_i.sort(key=lambda x: x[1])
            prev_y = plots_on_i[0][1]
            is_left_same_side = False
            is_right_same_side = False
            for curr_plot in plots_on_i:
                if (i - 1, curr_plot[1]) not in region:
                    if curr_plot[1] - 1 != prev_y:
                        is_left_same_side = False
                    if not is_left_same_side:
                        sides += 1
                    is_left_same_side = True
                else:
                    is_left_same_side = False
                if (i + 1, curr_plot[1]) not in region:
                    if curr_plot[1] - 1 != prev_y:
                        is_right_same_side = False
                    if not is_right_same_side:
                        sides += 1
                    is_right_same_side = True
                else:
                    is_right_same_side = False
                prev_y = curr_plot[1]
        result += sides * len(region)
    return result


def solve_part_two():
    plants = defaultdict(list)
    for j, row in enumerate(input):
        for i, plant in enumerate(row):
            plants[plant].append((i, j))

    plants = sperate_to_regions(plants)
    total_fence_price = 0
    for plant, regions in plants.items():
        total_fence_price += calcualate_discount_price(regions)
    print(total_fence_price)

solve_part_two()