# ------------------------Stack extending List-----------
class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack Is empty.")

    def size(self):
        return len(self)

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            return IndexError("Stack is empty.")

    def insert(self):
        raise "Insertion not Possible. In Stack Object."

    def __iter__(self):
        raise StopIteration("Stack Object is not iterable.")


# ---------------Testing code----------
myStack = Stack()
print("Stack is empty or not:", myStack.is_empty())
myStack.push(20)
myStack.push(40)
myStack.push(60)
myStack.push(80)
# myStack.insert()
print("Last element of the stack is :", myStack.pop())
print("Size of the element:", myStack.size())
print("Peek element of the stack is :", myStack.peek())
