from common_code import LinkedList


def reverse_linked_list():
    myCuteList: LinkedList = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(myCuteList)
    myCuteList.reverse_set_of_list_with_size(3)
    print(myCuteList)


if __name__ == '__main__':
    reverse_linked_list()
