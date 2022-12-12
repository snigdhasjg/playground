import operator
import re
from functools import reduce


class Monkey:
    if_false_monkey = None
    if_true_monkey = None
    common_divisor = None

    def __init__(self, monkey_details):
        """
        Monkey 0:
          Starting items: 79, 98
          Operation: new = old * 19
          Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
        """
        pattern = re.compile('''Monkey (\\d+):
\\s{2}Starting items: ((\\d+)(, \\d+)*)
\\s{2}Operation: new = old ([*+]) (\\w+)
\\s{2}Test: divisible by (\\d+)
\\s{4}If true: throw to monkey (\\d+)
\\s{4}If false: throw to monkey (\\d+)''')
        search_result = pattern.search(monkey_details)

        self.monkey_id = int(search_result.group(1))
        self.item_in_hand = list(map(int, search_result.group(2).split(', ')))
        self.operator = operator.mul if search_result.group(5) == '*' else operator.add
        self.operand = search_result.group(6)
        self.divisor = int(search_result.group(7))
        self.if_true_monkey_id = int(search_result.group(8))
        self.if_false_monkey_id = int(search_result.group(9))
        self.add_item_count = len(self.item_in_hand)

    def update(self, monkeys):
        self.if_true_monkey = monkeys[self.if_true_monkey_id]
        self.if_false_monkey = monkeys[self.if_false_monkey_id]
        self.common_divisor = reduce(operator.mul, [monkeys[monkey_id].divisor for monkey_id in monkeys])

    def add_item(self, item_value):
        self.add_item_count += 1
        self.item_in_hand.append(item_value)

    def operation(self, value):
        if self.operand == 'old':
            return self.operator(value, value)
        return self.operator(value, int(self.operand))

    def throw_all_item(self):
        for _ in range(len(self.item_in_hand)):
            item_inspecting = self.item_in_hand.pop(0)
            item_updated_value = (self.operation(item_inspecting) // 3) % self.common_divisor
            if item_updated_value % self.divisor == 0:
                self.if_true_monkey.add_item(item_updated_value)
            else:
                self.if_false_monkey.add_item(item_updated_value)

    def total_inspection_count(self):
        return self.add_item_count - len(self.item_in_hand)

    def __str__(self):
        return 'Monkey {} ({}): {}'.format(
            self.monkey_id,
            self.total_inspection_count(),
            ', '.join(map(str, self.item_in_hand))
        )


def parse_input():
    with open('input/day11.txt') as file:
        monkey_details = file.read().split('\n\n')

    monkeys = {}
    for each in monkey_details:
        monkey = Monkey(each)
        monkeys[monkey.monkey_id] = monkey

    return monkeys


def process():
    monkeys = parse_input()
    for monkey_id in monkeys:
        # print(monkeys[monkey_id])
        monkey = monkeys[monkey_id]
        monkey.update(monkeys)

    for _ in range(20):
        for monkey_id in monkeys:
            monkeys[monkey_id].throw_all_item()

    print(reduce(
        operator.mul,
        sorted([monkeys[monkey_id].total_inspection_count() for monkey_id in monkeys])[-2:]
    ))


if __name__ == '__main__':
    process()
