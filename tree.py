class Node(object):
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left_children = left
        self.right_children = right

    def add_child(self, value):
        child = Node(value)
        self.__add_child(child)
        return self

    def __add_child(self, child) -> None:
        if child.value < self.value:
            if self.left_children:
                self.left_children.__add_child(child)
            else:
                self.left_children = child
        elif child.value > self.value:
            if self.right_children:
                self.right_children.__add_child(child)
            else:
                self.right_children = child
        else:
            print("Value already exists {}".format(child.value))

    def __str__(self, level=0) -> str:
        ret = self.left_children.__str__(level + 1) if self.left_children else ""
        ret += "\t" * level + repr(self.value) + "\n"
        ret += self.right_children.__str__(level + 1) if self.right_children else ""
        return ret
