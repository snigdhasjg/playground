import logging
import math
from dataclasses import dataclass

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
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
class DestinationSourceRange:
    destination_start: int
    destination_end: int
    source_start: int
    source_end: int

    def __lt__(self, other):
        """Used for sorting"""
        return self.source_start < other.source_start

    def __repr__(self):
        """Used for printing/logging"""
        return f'Source: ({self.source_start}, {self.source_end}) -> Destination: ({self.destination_start}, {self.destination_end})'


@dataclass
class DestinationSourceMap:
    """
        the destination range start, the source range start, and the range length
    """
    type: str
    raw_string_map: str

    def __post_init__(self):
        mapping = list(map(int, self.raw_string_map.split(' ')))

        self.range_length: int = mapping[2]

        self.destination_start: int = mapping[0]
        self.destination_end: int = self.destination_start + self.range_length - 1
        self.source_start: int = mapping[1]
        self.source_end: int = self.source_start + self.range_length - 1

    def destination_range(self, source_start, source_end):
        # Doesn't belong to this
        if source_end < self.source_start or source_start > self.source_end:
            return None

        overlapping_source_start = self.source_start if source_start <= self.source_start else source_start
        overlapping_source_end = self.source_end if source_end >= self.source_end else source_end

        start_diff = self.source_start - overlapping_source_start
        end_diff = self.source_end - overlapping_source_end

        return DestinationSourceRange(
            self.destination_start - start_diff, self.destination_end - end_diff,
            overlapping_source_start, overlapping_source_end
        )

    def does_source_belongs_to(self, source):
        return self.source_start <= source <= self.source_end

    def destination(self, source):
        diff = source - self.source_start
        dest = self.destination_start + diff
        LOG.debug(f'{self.type} {source} -> {dest}')
        return dest

    def __repr__(self):
        """Used for printing/logging"""
        return f'{self.raw_string_map} is {self.type}'


def parse_raw_input(mapping_array: list[str]) -> list[list[DestinationSourceMap]]:
    mappings = []
    for string_mapping in mapping_array:
        mapping = string_mapping.split('\n')

        mapping_type = mapping[0].rstrip(':')
        values = [DestinationSourceMap(mapping_type, x) for x in mapping[1:]]
        mappings.append(values)

    return mappings


def part1(raw_input):
    raw_input_array = raw_input.split('\n\n')
    seeds = list(map(int, raw_input_array[0].lstrip('seeds: ').split(' ')))
    mappings = parse_raw_input(raw_input_array[1:])

    def find_location(seed):
        LOG.debug(f'\nFinding location of seed: {seed}')
        source = seed
        for each_mappings in mappings:
            destination = None
            for each_map in each_mappings:
                if each_map.does_source_belongs_to(source):
                    destination = each_map.destination(source)
            if destination:
                source = destination
            else:
                LOG.debug('Maps to same destination')
        LOG.debug(f'Destination: {source}')
        return source

    lowest_location = math.inf

    for each_seed in seeds:
        lowest_location = min(find_location(each_seed), lowest_location)

    return lowest_location


def part2_example():
    return part1_example()


def part2(raw_input):
    raw_input_array = raw_input.split('\n\n')
    mappings = parse_raw_input(raw_input_array[1:])

    seeds = list(map(int, raw_input_array[0].lstrip('seeds: ').split(' ')))
    seeds_range = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

    min_location = math.inf

    for seed_start, seed_end in seeds_range:
        to_process_source = [(seed_start, seed_end)]
        LOG.debug(f'Initial seed value: {to_process_source[0]}')

        for each_type_mappings in mappings:
            to_be_processed_destination = []
            for source_start, source_end in to_process_source:
                # Find all matching destination from mapping
                destinations: list[DestinationSourceRange] = list(sorted(filter(
                    lambda y: y is not None,
                    map(lambda x: x.destination_range(source_start, source_end), each_type_mappings)
                )))

                pointer = source_start
                for each_destination in destinations:
                    to_be_processed_destination.append(
                        (each_destination.destination_start, each_destination.destination_end))

                    if each_destination.source_start != pointer:
                        to_be_processed_destination.append((pointer, each_destination.source_start - 1))
                    pointer = each_destination.source_end + 1
                if pointer - 1 != source_end:
                    to_be_processed_destination.append((pointer, source_end))

            LOG.debug(f'Next set of source: {to_be_processed_destination}')
            to_process_source = to_be_processed_destination

        # Find minimum location
        min_location_this_run = min(to_process_source, key=lambda x: x[0])[0]
        LOG.info(f'Min location: {min_location_this_run}')
        min_location = min(min_location_this_run, min_location)

    return min_location
