class Seat:
    def __init__(self, seat_id) -> None:
        self.seat_id = seat_id
        self.lower = 0
        self.upper = 127
        self.left = 0
        self.right = 7

    def decode(self):
        for i in list(self.seat_id):
            self.binary_search(i)
        return (self.upper * 8) + self.right

    def binary_search(self, ins):
        if ins == 'F':
            mid = self.lower + ((self.upper - self.lower) // 2)
            self.upper = mid
        elif ins == 'B':
            mid = self.lower + ((self.upper - self.lower) // 2)
            self.lower = mid + 1
        elif ins == 'R':
            mid = self.left + ((self.right - self.left) // 2)
            self.left = mid + 1
        elif ins == 'L':
            mid = self.left + ((self.right - self.left) // 2)
            self.right = mid
        else:
            raise ValueError('Check why')


with open('input/day5.txt') as file:
    _max = -1
    all_ids = []
    for each_line in file:
        sid = Seat(each_line.strip()).decode()
        # print(sid)
        all_ids.append(sid)
        if sid > _max:
            _max = sid
    all_ids.sort()
    prev = 20
    for i in all_ids:
        if (i-prev) == 1:
            prev = i
        else:
            print(i)
            break
    print(all_ids)


if __name__ == '__main__':
    # print(_max)
    pass
