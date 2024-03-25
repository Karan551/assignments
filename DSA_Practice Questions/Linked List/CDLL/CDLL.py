class Node:
    def __init__(self, item=None, prev=None, next_ref=None):
        self.item = item
        self.prev = prev
        self.next = next_ref


class CDLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_node_object = Node(data)
        if self.is_empty():
            new_node_object.prev = new_node_object
            new_node_object.next = new_node_object
            self.start = new_node_object
        else:
            new_node_object.next = self.start
            new_node_object.prev = self.start.prev
            self.start.prev.next = new_node_object
            self.start = new_node_object
        # Increment the value of counter
        self.count += 1

    def insert_at_last(self, data):
        new_node_object = Node(data)
        if self.is_empty():
            new_node_object.prev = new_node_object
            new_node_object.next = new_node_object
            self.start = new_node_object
        else:
            new_node_object.prev = self.start.prev
            new_node_object.next = self.start.prev.next
            self.start.prev.next = new_node_object
            self.start.prev = new_node_object
        # Increment the value of counter
        self.count += 1

    def search(self, search_data):
        if not self.is_empty():
            temp = self.start
            while temp.next is not self.start.prev.next:
                if temp.item == search_data:
                    return True
                temp = temp.next
            # To check the last Node value with search_data
            if temp.item == search_data:
                return True
            else:
                return False
        else:
            return "CDLL is empty."

    def insert_after(self, search_data, insert_data):
        if not self.is_empty() and self.search(search_data):
            # Increment the value of counter.
            self.count += 1
            new_node_object = Node(insert_data)
            temp = self.start
            # If CDLL contains only one Node, then do this.
            if temp.prev == temp or temp.next == temp:
                new_node_object.prev = self.start
                new_node_object.next = self.start
                self.start.prev = new_node_object
                self.start.next = new_node_object
            else:
                if temp.item == search_data and temp.next != temp:
                    new_node_object.prev = temp
                    new_node_object.next = temp.next
                    temp.next.prev = new_node_object
                    temp.next = new_node_object
                else:
                    while temp.next is not self.start.prev.next:
                        if temp.item == search_data:
                            new_node_object.prev = temp
                            new_node_object.next = temp.next
                            temp.next.prev = new_node_object
                            temp.next = new_node_object
                            break
                        temp = temp.next
                    else:
                        if temp.item == search_data:
                            new_node_object.prev = temp
                            new_node_object.next = temp.next
                            temp.next = new_node_object
                            self.start.prev = new_node_object
        else:
            return "CDLL is empty."

    def printList(self):
        if self.is_empty():
            return "CDLL is empty."
        temp = self.start
        while temp.next is not self.start.prev.next:
            print(temp.item, end=" ")
            temp = temp.next
        # To print last Node data
        print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
            # Decrement the value of counter.
            self.count -= 1
        else:
            return "CDLL is empty."

    def delete_last(self):
        if not self.is_empty():
            if self.start.prev == self.start or self.start.next == self.start:
                self.start = None
            else:
                # print("this is second last node item:", self.start.prev.prev.item)
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
            # Decrement the value of counter.
            self.count -= 1
        else:
            return "CDLL is empty."

    def length(self):
        return self.count


# ---------------Testing Code-------------
myList = CDLL()
print("CDLL is empty or not:", myList.is_empty())
# myList.insert_at_start(80)
myList.insert_at_start(40)
myList.insert_at_start(20)
myList.insert_at_last(100)
# myList.insert_at_last(120)
myList.printList()

# print(f"List contains {80}:-",myList.search(80))
# print("CDLL is empty or not:", myList.is_empty())
# myList.insert_after(100, 500)
# myList.delete_first()
myList.delete_last()
myList.delete_last()
# myList.delete_last()
# myList.delete_last()

print("After Deletion")
myList.printList()
print("CDLL length is :", myList.length())
