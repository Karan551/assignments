class Deque:
    def __init__(self):
        self.my_deque = []

    def is_empty(self):
        return len(self.my_deque) == 0

    def insert_front(self, data):
        self.my_deque.insert(0, data)

    def insert_rear(self, data):
        self.my_deque.append(data)

    def delete_rear(self):
        if not self.is_empty():
            self.my_deque.pop()
        else:
            raise IndexError("Deque is empty.")

    def delete_front(self):
        if not self.is_empty():
            self.my_deque.pop(0)
        else:
            raise IndexError("Deque is empty.")

    def get_front(self):
        if not self.is_empty():
            return self.my_deque[0]
        else:
            raise IndexError("Deque Is empty.")

    def get_rear(self):
        if not self.is_empty():
            return self.my_deque[-1]
        else:
            raise IndexError("Deque Is empty.")

    def size(self):
        return len(self.my_deque)


# ---------------------- Testing Code ---------
myDeque = Deque()
print("Deque is empty or not:", myDeque.is_empty())

myDeque.insert_front(80)
myDeque.insert_front(60)
myDeque.insert_front(40)
myDeque.insert_front(20)
myDeque.insert_rear(100)
print("This is the front element of Deque:", myDeque.get_front())
print("This is the rear element of Deque:", myDeque.get_rear())
print("Size of Deque is:", myDeque.size())
print("--------------------------------")
myDeque.delete_front()
myDeque.delete_rear()
print("This is the front element of Deque:", myDeque.get_front())
print("This is the rear element of Deque:", myDeque.get_rear())
print("Size of Deque is:", myDeque.size())
print("Deque is empty or not:", myDeque.is_empty())
