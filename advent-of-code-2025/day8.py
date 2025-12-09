import logging
import uuid

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.DEBUG
DAY = 8
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True


class Connection:
    def __init__(self):
        self.id: uuid.UUID = uuid.uuid4()
        self.nodes: set[JunctionBox] = set()

    def add_node(self, node: 'JunctionBox'):
        self.nodes.add(node)

    def __repr__(self):
        return f"{self.id}: {len(self.nodes)}"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Connection):
            return NotImplemented
        return self.id == other.id


class JunctionBox:
    def __init__(self, comma_separated_string: str):
        self.coordinate = tuple(map(int, comma_separated_string.split(',')))

        self.X = self.coordinate[0]
        self.Y = self.coordinate[1]
        self.Z = self.coordinate[2]

        self.connection: Connection = None

    def __hash__(self):
        return hash(self.coordinate)

    def __repr__(self):
        return f"{self.X},{self.Y},{self.Z}"

    def __eq__(self, other):
        if not isinstance(other, JunctionBox):
            return NotImplemented
        return self.X == other.X and self.Y == other.Y and self.Z == other.Z

    def circuit_size(self):
        return len(self.connection.nodes) if self.connection else 1

    def distance(self, another: 'JunctionBox'):
        squared = (self.X - another.X) ** 2 + (self.Y - another.Y) ** 2 + (self.Z - another.Z) ** 2
        return squared
        # return math.sqrt(squared)

    def make_connection(self, another: 'JunctionBox'):
        if not self.connection and not another.connection:
            new_connection = Connection()
            self.connection = new_connection
            another.connection = new_connection
            new_connection.add_node(self)
            new_connection.add_node(another)
            LOG.debug("Creating new connection %s", new_connection)
        elif self.connection and another.connection:
            if self.connection.id == another.connection.id:
                return
            old_connection = another.connection
            for each_node in another.connection.nodes:
                self.connection.add_node(each_node)
                each_node.connection = self.connection
            LOG.debug("Merge happened for connection %s with %s", self.connection, old_connection)
        elif self.connection:
            another.connection = self.connection
            self.connection.add_node(another)
            LOG.debug("Found self connection %s", self.connection)
        elif another.connection:
            self.connection = another.connection
            another.connection.add_node(self)
            LOG.debug("Found another connection %s", another.connection)


def part1_example():
    # return ""
    return """\
        162,817,812
        57,618,57
        906,360,560
        592,479,940
        352,342,300
        466,668,158
        542,29,236
        431,825,988
        739,650,466
        52,470,668
        216,146,977
        819,987,18
        117,168,530
        805,96,715
        346,949,466
        970,615,88
        941,993,340
        862,61,35
        984,92,344
        425,690,689"""


def part1(raw_input: str, max_connection=1000):
    parsed_input = list(map(JunctionBox, raw_input.splitlines()))
    total_length = len(parsed_input)

    distances = []

    for i in range(total_length):
        for j in range(i + 1, total_length):
            distance = parsed_input[i].distance(parsed_input[j])
            distances.append((parsed_input[i], parsed_input[j], distance))

    distances = sorted(distances, key=lambda x: x[2])
    LOG.debug("Total size of pairs: %s", len(distances))
    index = 0
    for each_path in distances:
        LOG.debug("%s: %s <-> %s: %s", index, each_path[0], each_path[1], each_path[2])
        each_path[0].make_connection(each_path[1])
        index += 1
        if index >= max_connection:
            break

    connections = list(sorted(
        set([each_node.connection for each_node in parsed_input if each_node.connection]),
        key=lambda x: len(x.nodes),
        reverse=True
    ))[:3]
    result = 1
    for each_connection in connections:
        LOG.info(each_connection)
        LOG.info("\t%s", "\n\t".join(map(str, each_connection.nodes)))
        result *= len(each_connection.nodes)

    return result


def part2_example():
    # return ""
    return """\
        162,817,812
        57,618,57
        906,360,560
        592,479,940
        352,342,300
        466,668,158
        542,29,236
        431,825,988
        739,650,466
        52,470,668
        216,146,977
        819,987,18
        117,168,530
        805,96,715
        346,949,466
        970,615,88
        941,993,340
        862,61,35
        984,92,344
        425,690,689"""


def part2(raw_input: str):
    parsed_input = list(map(JunctionBox, raw_input.splitlines()))
    total_length = len(parsed_input)

    distances = []

    for i in range(total_length):
        for j in range(i + 1, total_length):
            distance = parsed_input[i].distance(parsed_input[j])
            distances.append((parsed_input[i], parsed_input[j], distance))

    distances = sorted(distances, key=lambda x: x[2])
    LOG.debug("Total size of pairs: %s", len(distances))
    index = 0
    for each_path in distances:
        LOG.debug("%s: %s <-> %s: %s", index, each_path[0], each_path[1], each_path[2])
        each_path[0].make_connection(each_path[1])
        if each_path[0].circuit_size() == total_length:
            return each_path[0].X * each_path[1].X
        index += 1

    return None
