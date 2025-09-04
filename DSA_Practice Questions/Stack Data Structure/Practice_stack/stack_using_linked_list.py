class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class Stack:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data):
        new_node = Node(data)
        if not self.is_empty():

            pass
        else:
            self.start = new_node
