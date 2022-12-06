with open('input/day6.txt') as file:
    signal = file.read().strip()


def process_signal(_signal, distinct_char=4):
    for i in range(len(_signal) - distinct_char):
        if len(set(_signal[i:i + distinct_char])) == distinct_char:
            return i + distinct_char


if __name__ == '__main__':
    print(process_signal(signal, 14))
