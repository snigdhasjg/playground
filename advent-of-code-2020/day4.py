import re


def take_input():
    users_data = []
    with open('input/day4.txt') as file:
        user_data = {}

        for each_line in file:
            if each_line == '\n':
                if len(user_data) != 0:
                    users_data.append(user_data)
                user_data = {}
            key_values = each_line.split(' ')
            for key_value in key_values:
                key_value_list = key_value.split(':')
                if len(key_value_list) == 2:
                    user_data[key_value_list[0]] = key_value_list[1].strip()
        if len(user_data) != 0:
            users_data.append(user_data)
    return users_data


def is_valid_field_present():
    count_valid = 0
    for user_data in take_input():
        if User(user_data).is_valid():
            # print('valid', user_data)
            count_valid += 1
        # else:
        # print('invalid', user_data)
    print(count_valid)


def is_valid(user_data: dict):
    required_field = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in required_field:
        if i in user_data.keys():
            pass
        else:
            return False
    return True


class User:
    _required_field = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, user_data: dict) -> None:
        self.user_data = user_data
        self.byr: str = user_data.get('byr')
        self.iyr: str = user_data.get('iyr')
        self.eyr: str = user_data.get('eyr')
        self.hgt: str = user_data.get('hgt')
        self.hcl: str = user_data.get('hcl')
        self.ecl: str = user_data.get('ecl')
        self.pid: str = user_data.get('pid')

    def is_valid(self):
        return self._is_valid_number(self.byr, 1920, 2002) \
               and self._is_valid_number(self.iyr, 2010, 2020) \
               and self._is_valid_number(self.eyr, 2020, 2030) \
               and self._is_valid_color() and self._is_valid_height() and self._is_valid_eye_color() \
               and self._is_valid_passport()

    def _is_valid_passport(self):
        try:
            assert self.hgt is not None
            assert re.search('^[0-9]{9}$', self.pid) is not None
        except (AssertionError, ValueError, TypeError):
            return False
        return True

    def _is_valid_eye_color(self):
        valid_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        try:
            assert self.hgt is not None
            assert self.ecl in valid_color
        except (AssertionError, ValueError):
            return False
        return True

    def _is_valid_height(self):
        try:
            assert self.hgt is not None
            if self.hgt.endswith('cm'):
                assert 150 <= int(self.hgt.strip('cm')) <= 193
            elif self.hgt.endswith('in'):
                assert 59 <= int(self.hgt.strip('in')) <= 76
            else:
                return False
        except (AssertionError, ValueError):
            return False
        return True

    def _is_valid_color(self):
        try:
            assert self.hcl is not None
            assert re.search('^#([a-fA-F0-9]{6})$', self.hcl) is not None
        except (AssertionError, ValueError):
            return False
        return True

    def _is_valid_number(self, number: str, lower: int, upper: int):
        try:
            assert number is not None
            assert len(number) == 4
            num = int(number)
            assert lower <= num <= upper
        except (AssertionError, ValueError):
            return False
        return True


if __name__ == '__main__':
    is_valid_field_present()
