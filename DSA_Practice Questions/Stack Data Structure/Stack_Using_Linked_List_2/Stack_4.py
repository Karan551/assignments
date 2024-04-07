# import SLL_2 as S
from SLL_2 import *


class Stack:
    def __init__(self):
        self.stack = SLL()
        self.count = 0

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, data):
        self.stack.insert_at_start(data)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.stack.delete_first()
            self.count -= 1
        else:
            raise IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.stack.start.item
        else:
            raise IndexError("Stack is empty.")

    def size(self):
        return self.count


# -------------Testing Code-----------
myStack = Stack()
print("Stack is empty or not:", myStack.is_empty())
myStack.push(20)
myStack.push(40)
myStack.push(60)
myStack.push(80)
print("The top element of the Stack is:", myStack.peek())
print("Length of the Stack is:", myStack.size())
myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
print("The top element of the Stack is:", myStack.peek())
print("Length of the Stack is:", myStack.size())
print("Stack is empty or not:", myStack.is_empty())
