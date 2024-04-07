from SLL import *


class Stack(SLL):

    def is_empty(self):
        return super().is_empty()

    def push(self, item):
        self.insert_at_start(item)

    def pop(self):
        if not self.is_empty():
            self.delete_first()
        else:
            raise IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty.")

    def size(self):
        return self.length()

    def insert(self):
        raise IndexError("Insertion is not possible.")


# -------------Testing Code-----------
myStack = Stack()
# myStack.insert()
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
