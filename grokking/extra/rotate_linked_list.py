from common_code import LinkedList


def rotate_linked_list():
    myCuteList: LinkedList = LinkedList([1, 2, 3, 4, 5])
    print(myCuteList)
    myCuteList.rotate(5)
    print(myCuteList)


if __name__ == '__main__':
    rotate_linked_list()
