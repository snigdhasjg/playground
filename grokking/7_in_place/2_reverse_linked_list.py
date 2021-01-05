from common_code import LinkedList


def reverse_linked_list():
    myCuteList: LinkedList = LinkedList([1])
    print(myCuteList)
    myCuteList.reverse()
    print(myCuteList)


if __name__ == '__main__':
    reverse_linked_list()
