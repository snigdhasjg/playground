from common_code import Node, LinkedList


def findIfCycleExists():
    myCuteList: LinkedList = LinkedList([1, 2, 4, 5, 6, 7, 8])
    myCuteList.add_cycle(3)
    print(myCuteList)

    return myCuteList.is_cycle_exists()


if __name__ == '__main__':
    print(findIfCycleExists())
