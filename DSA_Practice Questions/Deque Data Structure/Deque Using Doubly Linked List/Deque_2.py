class Node:
    def __init__(self, prev=None, item=None, next_ref=None):
        self.prev = prev
        self.item = item
        self.next = next_ref


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front is None

    def insert_front(self, data):
        new_node_object = Node(None, data)
        # self.front = new_node_object
        if not self.is_empty():
            new_node_object.next = self.front
            self.front.prev = new_node_object
        else:
            self.rear = new_node_object
        self.front = new_node_object
        # Increment the value of counter
        self.item_count += 1

    def insert_rear(self, data):
        new_node_object = Node(self.rear, data)
        if not self.is_empty():
            self.rear.next = new_node_object
        else:
            self.front = new_node_object
        self.rear = new_node_object
        # Increment the value of counter
        self.item_count += 1

    def delete_front(self):
        if not self.is_empty():
            # If Deque has only one Node, Then do this.
            if self.front == self.rear:
                self.front = None
                self.rear = None
            # If Deque has minimum two Node, Then do this.
            else:
                self.front.next.prev = None
                self.front = self.front.next
            # Decrement the value of counter
            self.item_count -= 1
        else:
            IndexError("Deque Is Empty.")

    def delete_rear(self):
        if not self.is_empty():
            # If Deque has only one Node, Then do this.
            if self.front == self.rear:
                self.front = None
                self.rear = None
            # If Deque has minimum two Nodes, Then do this.
            else:
                self.rear.prev.next = None
                self.rear = self.rear.prev
            # Decrement the value of counter
            self.item_count -= 1
        else:
            IndexError("Deque is Empty.")

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            IndexError("Deque is Empty.")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            IndexError("Deque is Empty.")

    def size(self):
        return self.item_count


# --------------Testing Code-------------
myDeque = Deque()
print("Deque Is empty or not:", myDeque.is_empty())
myDeque.insert_front(60)
myDeque.insert_front(40)
myDeque.insert_front(20)
myDeque.insert_rear(80)
myDeque.insert_rear(100)
# myDeque.delete_front()
# myDeque.delete_front()
# myDeque.delete_front()
# myDeque.delete_front()
# myDeque.delete_rear()
# myDeque.delete_rear()
# myDeque.delete_rear()
# myDeque.delete_rear()
# myDeque.delete_rear()
print("This is front item:", myDeque.get_front())
print("This is rear item:", myDeque.get_rear())
print("Size of the Deque is:", myDeque.size())
print("Deque Is empty or not:", myDeque.is_empty())
