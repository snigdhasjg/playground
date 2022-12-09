def parse_input():
    commands = []
    current_command = None
    current_output = []
    with open('input/day7.txt') as file:
        for line in file:
            if line.startswith('$ '):
                if current_command:
                    if current_command.startswith('cd '):
                        commands.append(current_command)
                    else:
                        commands.append(current_output)
                current_output = []
                current_command = line.strip().removeprefix('$ ')
            else:
                current_output.append(line.strip())
        if current_command.startswith('cd '):
            commands.append(current_command)
        else:
            commands.append(current_output)
    return commands


class Directory:
    def __init__(self, name, parent=None):
        self.__name = name
        self.__sub_directories = {}
        self.__files = []
        self.__parent = parent

    def sub_directory(self, name):
        if name not in self.__sub_directories:
            self.__sub_directories[name] = Directory(name, self)
        return self.__sub_directories[name]

    def file(self, size_and_name: str):
        san = size_and_name.split(' ')
        file = File(san[1], int(san[0]))
        self.__files.append(file)
        return file

    def parent_directory(self):
        return self.__parent

    def total_size(self):
        total_size = 0
        if len(self.__sub_directories) != 0:
            for each_directory_name in self.__sub_directories:
                total_size += self.__sub_directories[each_directory_name].total_size()
        if len(self.__files) != 0:
            total_size += sum(map(lambda x: x.size(), self.__files))
        return total_size

    def __str__(self):
        return '- {} (dir, size={})'.format(self.__name, self.total_size())

    def tree(self, level=0):
        print('\t' * level, end='')
        print(self)
        next_level = level + 1
        for each in self.__sub_directories:
            self.__sub_directories[each].tree(next_level)
        for each in self.__files:
            print('\t' * next_level, end='')
            print(each)

    def part1(self):
        total = 0
        current_node_size = self.total_size()
        if current_node_size <= 100000:
            total += current_node_size
        return total + sum(self.__sub_directories[each].part1() for each in self.__sub_directories)

    def __all_directory_size(self, sizes=None):
        if sizes is None:
            sizes = []
        sizes.append(self.total_size())
        [self.__sub_directories[each].__all_directory_size(sizes) for each in self.__sub_directories]
        return sizes

    def part2(self, free_space_required):
        return min(filter(lambda x: x >= free_space_required, self.__all_directory_size()))


class File:
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def __str__(self):
        return '- {} (file, size={})'.format(self.__name, self.__size)

    def size(self):
        return self.__size


root_directory = Directory('/')


def process():
    current_directory = None
    for command in parse_input():
        if type(command) == str:
            relative_path = command.removeprefix('cd ')
            if relative_path == '/':
                current_directory = root_directory
            elif relative_path == '..':
                current_directory = current_directory.parent_directory()
            else:
                current_directory = current_directory.sub_directory(relative_path)
        else:
            for ls_output_line in command:
                if ls_output_line.startswith('dir '):
                    current_directory.sub_directory(ls_output_line.removeprefix('dir '))
                else:
                    current_directory.file(ls_output_line)


if __name__ == '__main__':
    process()
    root_directory.tree()
    print(root_directory.part1())
    print(root_directory.part2(30000000 - (70000000 - root_directory.total_size())))
