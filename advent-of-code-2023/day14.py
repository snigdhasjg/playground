import logging

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 14
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#...."""


class Group:
    def __init__(self, rocks: str, starting_pos):
        self.rocks = rocks
        self.rounded_rocks_count = rocks.count('O')
        self.starting_pos = starting_pos

    def load(self):
        return sum(map(lambda x: self.starting_pos - x, range(self.rounded_rocks_count)))

    def __repr__(self):
        return f'{self.starting_pos}: {self.rocks}({self.rounded_rocks_count})'


class Line:
    def __init__(self, rocks: str):
        self.groups = []
        visited_length = len(rocks)
        for idx, group in enumerate(rocks.split('#')):
            if 'O' in group:
                self.groups.append(Group(group, visited_length))
            visited_length = visited_length - 1 - len(group)

        LOG.debug(self)

    def load(self):
        return sum(map(lambda x: x.load(), self.groups))

    def __repr__(self):
        return f'[\n\t{"\n\t".join(map(repr, self.groups))} \n] -> {self.load()}'


def part1(raw_input: str):
    raw_input_lines = raw_input.splitlines()
    lines = [''] * len(raw_input_lines[0])
    for each_row in raw_input_lines:
        for idx, each_char in enumerate(each_row):
            lines[idx] += each_char

    return sum([Line(rocks).load() for rocks in lines])


def part2_example():
    return """\
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#...."""


class Panel:
    def __init__(self, raw_input):
        self.platform = list(map(list, raw_input.splitlines()))
        self.x_len = len(self.platform[0])
        self.y_len = len(self.platform)

        LOG.debug(self)

    def __hash__(self):
        return hash(repr(self))

    def load(self):
        total_sum = 0
        for x in range(self.x_len):
            line_sum = 0
            for y in range(self.y_len):
                if self.platform[y][x] == 'O':
                    line_sum += self.y_len - y
            total_sum += line_sum

        return total_sum

    def cycle(self):
        def north():
            LOG.debug('\nTilting north')
            for x in range(self.x_len):
                last_empty_space = -1
                for y in range(self.y_len):
                    current_value = self.platform[y][x]
                    if last_empty_space == -1:
                        if current_value == '.':
                            last_empty_space = y
                    elif current_value == 'O':
                        self.platform[last_empty_space][x] = 'O'
                        self.platform[y][x] = '.'
                        last_empty_space += 1
                    elif current_value == '#':
                        last_empty_space = -1
            LOG.debug(self)

        def south():
            LOG.debug('\nTilting south')
            for x in range(self.x_len):
                last_empty_space = -1
                for y in range(self.y_len - 1, -1, -1):
                    current_value = self.platform[y][x]
                    if last_empty_space == -1:
                        if current_value == '.':
                            last_empty_space = y
                    elif current_value == 'O':
                        self.platform[last_empty_space][x] = 'O'
                        self.platform[y][x] = '.'
                        last_empty_space -= 1
                    elif current_value == '#':
                        last_empty_space = -1
            LOG.debug(self)

        def west():
            LOG.debug('\nTilting west')
            for y in range(self.y_len):
                last_empty_space = -1
                for x in range(self.x_len):
                    current_value = self.platform[y][x]
                    if last_empty_space == -1:
                        if current_value == '.':
                            last_empty_space = x
                    elif current_value == 'O':
                        self.platform[y][last_empty_space] = 'O'
                        self.platform[y][x] = '.'
                        last_empty_space += 1
                    elif current_value == '#':
                        last_empty_space = -1
            LOG.debug(self)

        def east():
            LOG.debug('\nTilting east')
            for y in range(self.y_len):
                last_empty_space = -1
                for x in range(self.x_len - 1, -1, -1):
                    current_value = self.platform[y][x]
                    if last_empty_space == -1:
                        if current_value == '.':
                            last_empty_space = x
                    elif current_value == 'O':
                        self.platform[y][last_empty_space] = 'O'
                        self.platform[y][x] = '.'
                        last_empty_space -= 1
                    elif current_value == '#':
                        last_empty_space = -1
            LOG.debug(self)

        north()
        west()
        south()
        east()

        LOG.debug('\nPost cycle')
        LOG.debug(self)

    def __repr__(self):
        return '\n'.join(map(lambda x: ''.join(x), self.platform))


def part2(raw_input: str):
    panel = Panel(raw_input)
    hashes = {hash(panel): 0}
    loads = []

    match = (0, 0)
    for i in range(1, 1000000001):
        panel.cycle()
        panel_hash = hash(panel)
        loads.append(panel.load())
        if panel_hash in hashes:
            match = (hashes[panel_hash], i)
            LOG.debug(f'Found cycle at {i} matches with {hashes[panel_hash]}')
            break
        hashes[panel_hash] = i

    cycle_length = match[1] - match[0]
    mod_value = (1000000000 - match[0]) % cycle_length
    return loads[match[0] + mod_value - 1]
