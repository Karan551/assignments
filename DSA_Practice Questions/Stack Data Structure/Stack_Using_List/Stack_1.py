class Stack:
    def __init__(self):
        self.myStack = []

    def is_empty(self):
        return len(self.myStack) == 0

    def push(self, data):
        self.myStack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.myStack.pop()
        else:
            return IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.myStack[-1]
        else:
            return IndexError("Stack is empty.")

    def size(self):
        return len(self.myStack)


# -------------------Testing Code----------
myStack = Stack()
print("Stack is empty or not  :", myStack.is_empty())
myStack.push(20)
myStack.push(40)
myStack.push(60)
myStack.push(80)
myStack.pop()
print("Length of the stack:", myStack.size())
print("Top (last) element of a stack:", myStack.peek())
print("Stack is empty or not :", myStack.is_empty())
