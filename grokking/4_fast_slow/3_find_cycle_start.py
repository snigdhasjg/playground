from common_code import Node, LinkedList


def findIfCycleStartNode():
    myCuteList: LinkedList = LinkedList([1, 2, 3, 4, 5, 6, 7])
    myCuteList.add_cycle(0)
    print(myCuteList)

    slow: Node = myCuteList.get_head()
    fast: Node = slow
    cycle_exists: bool = False
    # find a point within cycle
    while slow is not None and fast is not None:
        slow = slow.next_node()
        fast_next_node: Node = fast.next_node()
        if fast_next_node is None:
            break
        fast = fast_next_node.next_node()
        if slow == fast:
            cycle_exists = True
            break

    if not cycle_exists:
        return None
    # determine length of the cycle
    length_of_cycle = 0
    while slow.next_node() != fast:
        slow = slow.next_node()
        length_of_cycle += 1
    length_of_cycle += 1

    # find start of the loop
    first_pointer: Node = myCuteList.get_head()
    second_pointer: Node = first_pointer
    # forward second pointer by length of the cycle
    for _ in range(length_of_cycle):
        second_pointer = second_pointer.next_node()
    # forward both till they meet
    while first_pointer != second_pointer:
        first_pointer = first_pointer.next_node()
        second_pointer = second_pointer.next_node()

    return first_pointer


if __name__ == '__main__':
    print(findIfCycleStartNode())
