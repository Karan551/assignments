class Stack:

    def __init__(self):
        self.my_stack = []

    def is_empty(self):
        return len(self.my_stack) == 0

    def push(self, data):
        self.my_stack.append(data)

    def pop(self):
        if not self.is_empty():
            self.my_stack.pop()
        else:
            raise ValueError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.my_stack[-1]
        else:
            raise ValueError("Stack is empty.")

    def size(self):
        return len(self.my_stack)


# ----------------------------- Testing Code----------------
my_stack = Stack()
print("stack is empty or not::", my_stack.is_empty())
my_stack.push(80)
my_stack.push(60)
my_stack.push(40)
my_stack.push(20)

my_stack.pop()
my_stack.pop()
my_stack.pop()
# my_stack.pop()
print(my_stack.peek())
print("stack is empty or not::", my_stack.is_empty())
