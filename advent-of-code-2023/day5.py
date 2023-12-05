import logging
import math
from dataclasses import dataclass

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.INFO
DAY = 5
DEVELOPMENT_PHASE = False
PART_1_ENABLE = False
PART_2_ENABLE = True


def part1_example():
    return """\
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48
        
        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15
        
        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4
        
        water-to-light map:
        88 18 7
        18 25 70
        
        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13
        
        temperature-to-humidity map:
        0 69 1
        1 0 69
        
        humidity-to-location map:
        60 56 37
        56 93 4"""


@dataclass
class DestinationSourceMap:
    """
        the destination range start, the source range start, and the range length
    """
    type: str
    raw_string_map: str

    def __post_init__(self):
        mapping = list(map(int, self.raw_string_map.split(' ')))

        self.destination_start: int = mapping[0]
        self.source_start: int = mapping[1]
        self.source_end: int = mapping[1] + mapping[2] - 1
        self.range_length: int = mapping[2]

    def does_belongs_to(self, source):
        return self.source_start <= source <= self.source_end

    def destination(self, source):
        diff = source - self.source_start
        dest = self.destination_start + diff
        LOG.debug(f'{self.type} {source} -> {dest}')
        return dest

    def __repr__(self):
        return f'{self.raw_string_map} is {self.type}'


def parse_raw_input(mapping_array: list[str]) -> list[list[DestinationSourceMap]]:
    mappings = []
    for string_mapping in mapping_array:
        mapping = string_mapping.split('\n')

        mapping_type = mapping[0].rstrip(':')
        values = [DestinationSourceMap(mapping_type, x) for x in mapping[1:]]
        mappings.append(values)

    return mappings


def find_location(each_seed, mappings):
    LOG.debug(f'\nFinding location of seed: {each_seed}')
    source = each_seed
    for each_mappings in mappings:
        destination = None
        for each_map in each_mappings:
            if each_map.does_belongs_to(source):
                destination = each_map.destination(source)
        if destination:
            source = destination
        else:
            LOG.debug('Maps to same destination')
    LOG.debug(f'Destination: {source}')
    return source


def part1(raw_input):
    raw_input_array = raw_input.split('\n\n')
    seeds = list(map(int, raw_input_array[0].lstrip('seeds: ').split(' ')))
    mappings = parse_raw_input(raw_input_array[1:])

    lowest_location = math.inf

    for each_seed in seeds:
        lowest_location = min(find_location(each_seed, mappings), lowest_location)

    return lowest_location


def part2_example():
    return part1_example()


def part2(raw_input):

    raw_input_array = raw_input.split('\n\n')
    mappings = parse_raw_input(raw_input_array[1:])

    seeds = list(map(int, raw_input_array[0].lstrip('seeds: ').split(' ')))
    seeds_range = [tuple(seeds[i:i + 2]) for i in range(0, len(seeds), 2)]

    lowest_location = math.inf

    for each_seed_range in seeds_range:
        LOG.info(f'Each seed range: {each_seed_range}')
        for i in range(each_seed_range[1]):
            each_seed = each_seed_range[0] + i
            LOG.info(f'{i}: Seed id: {each_seed}')
            lowest_location = min(find_location(each_seed, mappings), lowest_location)

    return lowest_location
