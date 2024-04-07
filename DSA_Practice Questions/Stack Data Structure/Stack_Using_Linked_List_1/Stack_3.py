class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class Stack:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data):
        new_node_object = Node(data, self.start)
        self.start = new_node_object
        # Increment the value of counter
        self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            # Decrement the value of counter
            self.count -= 1
            return data
        else:
            raise IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty.")

    def size(self):
        return self.count


# ------------------Testing Code-------------
myStack = Stack()
print("Stack is empty", myStack.is_empty())
myStack.push(20)
myStack.push(40)
myStack.push(60)
myStack.push(80)
print("Size of the Stack is :", myStack.size())

print("The top element of the stack is :", myStack.peek())
myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
print("The top element of the stack is :", myStack.peek())
print("Size of the Stack is :", myStack.size())
print("Stack is empty", myStack.is_empty())
