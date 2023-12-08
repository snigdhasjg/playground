import logging
from collections import Counter
from enum import Enum

LOG = logging.getLogger(__name__)
LOG_LEVEL = logging.CRITICAL
DAY = 7
DEVELOPMENT_PHASE = False
PART_1_ENABLE = True
PART_2_ENABLE = True


def part1_example():
    return """\
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483"""


class HandType(Enum):
    FIVE_OF_A_KIND = 7  # AAAAA
    FOUR_OF_A_KIND = 6  # AA8AA
    FULL_HOUSE = 5  # 23332
    THREE_OF_A_KIND = 4  # TTT98
    TWO_PAIR = 3  # 23432
    ONE_PAIR = 2  # A23A4
    HIGH_CARD = 1  # 23456

    def __lt__(self, other):
        return self.value < other.value


class CardHand:

    def __init__(self, priority, get_hand_type, line):
        line_split = line.split(" ")

        self.value = line_split[0]
        self.bid_amount = int(line_split[1])

        self.type = get_hand_type(self.value)
        self.card_face_values = list(map(lambda x: priority[x], list(self.value)))

    def __repr__(self):
        return f'{self.value}({self.bid_amount}): {self.type}'

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for idx in range(5):
            if self.card_face_values[idx] != other.card_face_values[idx]:
                return self.card_face_values[idx] < other.card_face_values[idx]
        raise Exception("Both hands are same")

    def __eq__(self, other):
        return self.value == other.value


def part1(raw_input):
    priority = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'J': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1
    }

    def _type(all_cards: str):
        card_counter = Counter(all_cards)
        char_count = card_counter.most_common()
        if char_count[0][1] == 5:
            return HandType.FIVE_OF_A_KIND
        if char_count[0][1] == 4:
            return HandType.FOUR_OF_A_KIND
        if char_count[0][1] == 3:
            if char_count[1][1] == 2:
                return HandType.FULL_HOUSE
            return HandType.THREE_OF_A_KIND
        if char_count[0][1] == 2:
            if char_count[1][1] == 2:
                return HandType.TWO_PAIR
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    return calculate_winnings(priority, _type, raw_input)


def calculate_winnings(priority, _type, raw_input):
    hands = [CardHand(priority, _type, line) for line in raw_input.splitlines()]
    total_winnings = 0
    for idx, hand in enumerate(sorted(hands)):
        LOG.debug(f'{idx + 1}: {hand}')
        total_winnings += ((idx + 1) * hand.bid_amount)
    return total_winnings


def part2_example():
    return part1_example()


def part2(raw_input):
    priority = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'J': 1,
    }

    def _type(all_cards: str):
        card_counter = Counter(all_cards)
        count_of_j = card_counter['J'] if 'J' in card_counter else 0

        char_count = list(filter(lambda x: x[0] != 'J', card_counter.most_common()))  # [('a', 5), ('b', 2), ('r', 2)]
        if len(char_count) == 0:
            highest_count = ('J', count_of_j)
        else:
            highest_count = (char_count[0][0], char_count[0][1] + count_of_j)

        if highest_count[1] == 5:
            return HandType.FIVE_OF_A_KIND
        if highest_count[1] == 4:
            return HandType.FOUR_OF_A_KIND
        if highest_count[1] == 3:
            if char_count[1][1] == 2:
                return HandType.FULL_HOUSE
            return HandType.THREE_OF_A_KIND
        if highest_count[1] == 2:
            if char_count[1][1] == 2:
                return HandType.TWO_PAIR
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    return calculate_winnings(priority, _type, raw_input)
