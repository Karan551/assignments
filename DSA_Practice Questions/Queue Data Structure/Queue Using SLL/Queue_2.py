class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node_object = Node(data)
        if not self.is_empty():
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node_object
        else:
            self.front = new_node_object
        self.rear = new_node_object
        self.count += 1

    def dequeue(self):
        self.front = self.front.next
        self.count -= 1

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        raise IndexError("Queue is empty.")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        raise IndexError("Queue is empty.")

    def size(self):
        return self.count


# ------------------Testing Code--------------
myQueue = Queue()
print("Queue is empty :", myQueue.is_empty())
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)
print("This is the front element of the Queue:", myQueue.get_front())
print("This is the rear element of the Queue:", myQueue.get_rear())
print("Size of the Queue is :", myQueue.size())
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
print("---------------")
# print("This is the front element of the Queue:", myQueue.get_front())
print("This is the rear element of the Queue:", myQueue.get_rear())
print("Size of the Queue is :", myQueue.size())
print("Queue is empty :", myQueue.is_empty())
