import re


def process_input():
    with open('input/day5.txt') as file:
        __process_instruction = False
        supply_stack = []
        instructions = []
        for line in file:
            if line == '\n':
                __process_instruction = True
                continue
            if __process_instruction:
                line_search = re.search('move (\\d+) from (\\d+) to (\\d+)', line.strip())
                instructions.append((int(line_search.group(1)), int(line_search.group(2)), int(line_search.group(3))))
            else:
                supply_stack.append(list(line.strip()))
    return supply_stack, instructions


def part1():
    supply_stack, instructions = process_input()

    def process_instruction(_instruction):
        no_of_crates_to_move, source_stack_no, destination_stack_no = _instruction
        # for _ in range(no_of_crates_to_move):
        #     removed_stack = supply_stack[source_stack_no - 1].pop()
        #     supply_stack[destination_stack_no - 1].append(removed_stack)
        removed_stack = supply_stack[source_stack_no - 1][-no_of_crates_to_move:]
        supply_stack[source_stack_no - 1] = supply_stack[source_stack_no - 1][:-no_of_crates_to_move]
        supply_stack[destination_stack_no - 1].extend(removed_stack)

    for instruction in instructions:
        process_instruction(instruction)

    print(''.join([each_stack[-1] for each_stack in supply_stack]))


if __name__ == '__main__':
    part1()
