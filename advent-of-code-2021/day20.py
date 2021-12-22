# import time
# from os import system


def take_input():
    _lines = open("input/day20.txt").read().splitlines()
    _algorithm = list(_lines[0])

    _plane_dict = {}

    length_lines = len(_lines)
    for j in range(2, length_lines):
        each_line: str = _lines[j]
        for k in range(len(each_line)):
            pixel = each_line[k]
            if pixel == '#':
                _plane_dict[(j - 2, k)] = '#'

    return ImageAlgo(_algorithm, _plane_dict, Range(0, len(_lines) - 3, 0, len(_lines[2]) - 1))


class Range:
    def __init__(self, y_min, y_max, x_min, x_max):
        self.y_min = y_min
        self.y_max = y_max
        self.x_min = x_min
        self.x_max = x_max

    def next(self):
        return Range(self.y_min - 1, self.y_max + 1, self.x_min - 1, self.x_max + 1)


class ImageAlgo:
    reference_pos = {
        0: lambda idx: (idx[0] - 1, idx[1] - 1),
        1: lambda idx: (idx[0] - 1, idx[1]),
        2: lambda idx: (idx[0] - 1, idx[1] + 1),

        3: lambda idx: (idx[0], idx[1] - 1),
        4: lambda idx: idx,
        5: lambda idx: (idx[0], idx[1] + 1),

        6: lambda idx: (idx[0] + 1, idx[1] - 1),
        7: lambda idx: (idx[0] + 1, idx[1]),
        8: lambda idx: (idx[0] + 1, idx[1] + 1)
    }

    def __init__(self, _algorithm, _plane_dict, _range):
        self.__algorithm = _algorithm
        self.__plane_dict = _plane_dict
        self.__range: Range = _range

    def iterate(self, times):
        new_plane_dict = {}
        next_range = self.__range.next()

        def __get_value_from_dict(_space_index):
            return '1' if _space_index in self.__plane_dict else '0'

        def __get_index_of_algo(_space_index):
            out = ''
            for key in self.reference_pos:
                new_position = self.reference_pos[key](_space_index)
                if times % 2 == 0:
                    if new_position[0] <= next_range.y_min or new_position[0] >= next_range.y_max \
                            or new_position[1] <= next_range.x_min or new_position[1] >= next_range.x_max:
                        out += '1'
                        continue
                out += __get_value_from_dict(new_position)
            return int(out, 2)

        def __get_pixel_value(_space_index):
            return self.__algorithm[__get_index_of_algo(_space_index)]

        for y in range(next_range.y_min, next_range.y_max + 1):
            for x in range(next_range.x_min, next_range.x_max + 1):
                pixel = __get_pixel_value((y, x))
                if pixel == '#':
                    new_plane_dict[(y, x)] = pixel

        self.__plane_dict = new_plane_dict
        self.__range = next_range

        return len(new_plane_dict)

    def __str__(self):
        current_range = self.__range.next()
        out = ''
        for y in range(current_range.y_min, current_range.y_max + 1):
            for x in range(current_range.x_min, current_range.x_max + 1):
                if (y, x) in self.__plane_dict:
                    out += '#'
                else:
                    out += '.'
            out += '\n'
        return out


def iterate_print(image_algo: ImageAlgo, times):
    print(image_algo.iterate(times))
    # board = str(image_algo)
    # system('clear')
    # print(board)
    # time.sleep(3)


if __name__ == '__main__':
    algoWithImage = take_input()
    [iterate_print(algoWithImage, i) for i in range(1, 3)]
