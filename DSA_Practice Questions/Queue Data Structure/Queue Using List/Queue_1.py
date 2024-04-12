class Queue:
    def __init__(self):
        self.my_queue = []

    def is_empty(self):
        return len(self.my_queue) == 0

    def enqueue(self, data):
        self.my_queue.append(data)

    def dequeue(self):
        self.my_queue.pop(0)

    def get_front(self):
        return self.my_queue[0]

    def get_rear(self):
        return self.my_queue[-1]
        pass

    def size(self):
        return len(self.my_queue)


# -----------------Testing Code-------------------
myQueue = Queue()
print("Queue is empty or not:", myQueue.is_empty())
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)
print("This is the oldest element of the Queue:", myQueue.get_front())
print("This is the Latest element of the Queue:", myQueue.get_rear())
myQueue.dequeue()
myQueue.dequeue()
myQueue.enqueue(60)
print("---------------------------")
print("This is the oldest element of the Queue:", myQueue.get_front())
print("This is the Latest element of the Queue:", myQueue.get_rear())
print("Queue is empty or not:", myQueue.is_empty())
print("size of the queue:",myQueue.size())
