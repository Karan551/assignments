class Queue(list):

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.pop(0)

    def get_front(self):
        if not self.is_empty():
            return self[0]
        raise IndexError("Queue is empty.")

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        raise IndexError("Queue is empty.")

    def size(self):
        return len(self)

    def __iter__(self):
        raise StopIteration("Queue is not Iterable.")

    def insert(self):
        raise IndexError("Can't Insert Data in the queue.")

    def remove(self):
        raise IndexError("Can't remove any value in the Queue.")


# -------------------Testing Code --------------
myQueue = Queue()
print("Queue is empty or not:", myQueue.is_empty())
myQueue.enqueue(20)
myQueue.enqueue(40)
myQueue.enqueue(60)
myQueue.enqueue(80)
print("First element of the queue is:", myQueue.get_front())
print("Latest element of the queue is:", myQueue.get_rear())
print("Total element of the Queue is:", myQueue.size())
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()

print("-------------------------")
print("First element of the queue is:", myQueue.get_front())
print("Latest element of the queue is:", myQueue.get_rear())
print("Total element of the Queue is:", myQueue.size())
print("Queue is empty or not:", myQueue.is_empty())
# myQueue.insert()
