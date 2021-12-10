import sys

sys.setrecursionlimit(1800)

with open('input/day7.txt') as file:
    input_seq = [[int(i) for i in line.split(',')] for line in file][0]


def find_cost(dest):
    def delta(crab_position):
        if dest >= crab_position:
            return lambda x, y: x + y
        else:
            return lambda x, y: x - y

    def find_cost_each(crab_position, delta_function, cost=0, delta_cost=0):
        if crab_position == dest:
            # print(cost)
            return cost
        delta_cost += 1
        return find_cost_each(delta_function(crab_position, 1), delta_function, cost + delta_cost, delta_cost)

    return sum([find_cost_each(i, delta(i)) for i in input_seq])


def find_min_cost():
    _min = find_cost(0)
    count = 0
    for i in range(1, max(input_seq)):
        cost = find_cost(i)
        print(count, cost)
        count += 1
        if cost < _min:
            _min = cost

    return _min


if __name__ == '__main__':
    print(len(input_seq))
    print(find_min_cost())
