class Stack:
    def __init__(self):
        self.myStack = []

    def is_empty(self):
        return len(self.myStack) == 0

    def push(self, data):
        self.myStack.append(data)

    def pop(self):
        return self.myStack.pop()

    def peek(self):
        return self.myStack[-1]

    def length(self):
        return len(self.myStack)


# -------------------Testing Code----------
myStack = Stack()
print("Stack is empty or not  :", myStack.is_empty())
myStack.push(20)
myStack.push(40)
myStack.push(60)
myStack.push(80)
myStack.pop()
print("Length of the stack:", myStack.length())
print("Top (last) element of a stack:", myStack.peek())
print("Stack is empty or not :", myStack.is_empty())
