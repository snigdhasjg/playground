def take_input():
    _board = []
    for _l in open("input/day15.txt").read().splitlines():
        _board.append([int(_l[_x]) for _x in range(len(_l))])
    return _board


board = take_input()

distance = [[0] * 500 for _ in range(500)]
queue = [[(0, 0)]] + [[] for _ in range(10000)]  # [[(0,0)][][][][][][]...]
v = 0
while distance[499][499] == 0:
    for (y, x) in queue[v]:
        if v > distance[y][x]:
            continue
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= y + dy < 500 and 0 <= x + dx < 500:
                dt = ((board[(y + dy) % 100][(x + dx) % 100] + (y + dy) // 100 + (x + dx) // 100 - 1) % 9) + 1
                if distance[y + dy][x + dx] == 0:
                    distance[y + dy][x + dx] = v + dt
                    queue[v + dt].append((y + dy, x + dx))
    v += 1
print(distance[499][499])

if __name__ == '__main__':
    pass
