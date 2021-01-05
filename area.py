import math
from plindrome_time import get_limit


def area_of_triangle(a, b, c):
    half_of_perimeter = (a + b + c) / 2

    return math.sqrt(
        half_of_perimeter *
        (half_of_perimeter - a) *
        (half_of_perimeter - b) *
        (half_of_perimeter - c)
    )


def pythagoras(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def get_side(a, b, height):
    diff = abs(a - b)
    return pythagoras(diff, height)


def get_min_max(a, b, c, d, height):
    korno = pythagoras(height, height)
    # ABC #ACD
    ab = get_side(a, b, height)
    bc = get_side(b, c, height)
    cd = get_side(c, d, height)
    da = get_side(d, a, height)
    ac = get_side(a, c, korno)

    abc = area_of_triangle(ab, bc, ac)
    acd = area_of_triangle(ac, cd, da)

    return abc + acd


def new_pos(initial, time, velocity, height):
    if height == initial or initial == 0:
        return initial
    new_position = initial + (time * velocity)
    if new_position > height:
        return height
    if new_position < 0:
        return 0
    return new_position


def has_reached_end(a, b, c, d, height):
    if (height == a or a == 0) and \
            (height == b or b == 0) and \
            (height == c or c == 0) and \
            (height == d or d == 0):
        return True
    return False


def move(height, a, b, c, d, v1, v2, v3, v4):
    time = 0
    min_area = math.inf
    max_area = -1
    while True:
        if has_reached_end(a, b, c, d, height):
            break
        a = new_pos(a, time, v1, height)
        b = new_pos(b, time, v2, height)
        c = new_pos(c, time, v3, height)
        d = new_pos(d, time, v4, height)

        area = get_min_max(a, b, c, d, height)
        if area < min_area:
            min_area = area
        if area > max_area:
            max_area = area

        time += 1

    return round(4 * (max_area ** 2)), round(4 * (min_area ** 2))


if __name__ == '__main__':
    print(move(10, 5, 5, 5, 5, -1, 2, 1, -2))

