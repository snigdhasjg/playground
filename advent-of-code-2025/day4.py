import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 4
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        ..@@.@@@@.
        @@@.@.@.@@
        @@@@@.@.@@
        @.@@@@..@.
        @@.@@@@.@@
        .@@@@@@@.@
        .@.@.@.@@@
        @.@@@.@@@@
        .@@@@@@@@.
        @.@.@@@.@."""


def part1(raw_input: str):
    grid = list(map(lambda x: list(x), raw_input.splitlines()))
    grid_length_y = len(grid)
    grid_length_x = len(grid[0])
    position_to_check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def can_forklifts_access(y, x) -> bool:
        paper_roll_present_adjacent_positions = 0
        for each_dy, each_dx in position_to_check:
            if 0 <= y + each_dy < grid_length_y and 0 <= x + each_dx < grid_length_x:
                if grid[y + each_dy][x + each_dx] == '@':
                    paper_roll_present_adjacent_positions += 1
                if paper_roll_present_adjacent_positions >= 4:
                    return False
        return True

    def calculate_each_round():
        count = 0
        new_grid = []
        for i in range(grid_length_y):
            new_grid.append([])
            for j in range(grid_length_x):
                if grid[i][j] == "@" and can_forklifts_access(i, j):
                    count += 1
                    new_grid[i].append("x")
                else:
                    new_grid[i].append(grid[i][j])
        return count, new_grid

    return calculate_each_round()[0]


def part2_example():
    return """\
        ..@@.@@@@.
        @@@.@.@.@@
        @@@@@.@.@@
        @.@@@@..@.
        @@.@@@@.@@
        .@@@@@@@.@
        .@.@.@.@@@
        @.@@@.@@@@
        .@@@@@@@@.
        @.@.@@@.@."""


def part2(raw_input: str):
    grid = list(map(lambda x: list(x), raw_input.splitlines()))
    grid_length_y = len(grid)
    grid_length_x = len(grid[0])
    position_to_check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def can_forklifts_access(y, x) -> bool:
        paper_roll_present_adjacent_positions = 0
        for each_dy, each_dx in position_to_check:
            if 0 <= y + each_dy < grid_length_y and 0 <= x + each_dx < grid_length_x:
                if grid[y + each_dy][x + each_dx] == '@':
                    paper_roll_present_adjacent_positions += 1
                if paper_roll_present_adjacent_positions >= 4:
                    return False
        return True

    def calculate_each_round():
        count = 0
        new_grid = []
        for i in range(grid_length_y):
            new_grid.append([])
            for j in range(grid_length_x):
                if grid[i][j] == "@" and can_forklifts_access(i, j):
                    count += 1
                    new_grid[i].append("x")
                else:
                    new_grid[i].append(grid[i][j])
        return count, new_grid

    total_paper_rolls = 0
    while True:
        round_count, grid = calculate_each_round()
        total_paper_rolls += round_count
        if round_count == 0:
            break

    return total_paper_rolls
