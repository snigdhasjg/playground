import logging
import math

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 8
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        LLR

        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)"""


class Route:
    def __init__(self, line: str):
        paths = line.split(' = ')
        self.node = paths[0]
        left_right = paths[1].lstrip('(').rstrip(')').split(', ')
        self.left_node = left_right[0]
        self.right_node = left_right[1]

    def next(self, instruction):
        if instruction == 'L':
            return self.left_node
        return self.right_node

    def __repr__(self):
        return f'{self.node} = ({self.left_node}, {self.right_node})'


def parse_input(raw_input: str):
    all_lines = raw_input.splitlines()

    instructions = list(all_lines[0])
    routes = {}

    for line in all_lines[2:]:
        route = Route(line)
        routes[route.node] = route

    return instructions, routes


def part1(raw_input: str):
    instructions, routes = parse_input(raw_input)

    current_route_node = routes['AAA']
    index = 0
    count = 0
    while True:
        current_instruction = instructions[index]
        next_node = current_route_node.next(current_instruction)
        current_route_node = routes[next_node]
        count += 1

        if next_node == 'ZZZ':
            break

        index += 1
        if index == len(instructions):
            index = 0

    return count


def part2_example():
    return """\
        LR

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)"""


def part2(raw_input):
    instructions, routes = parse_input(raw_input)
    LOG.debug(f'Total no of instruction: {len(instructions)}')

    current_route_nodes = [v for k, v in routes.items() if k.endswith('A')]
    LOG.debug(f'Node starts with A: {list(map(lambda x: x.node, current_route_nodes))}')

    def _count_to_each_z(route: Route):
        index = 0
        count = 0
        while True:
            current_instruction = instructions[index]
            next_node = route.next(current_instruction)
            route = routes[next_node]
            count += 1

            if next_node.endswith('Z'):
                break

            index += 1
            if index == len(instructions):
                index = 0

        return count

    individual_node_count = list(map(_count_to_each_z, current_route_nodes))
    return math.lcm(*individual_node_count)
