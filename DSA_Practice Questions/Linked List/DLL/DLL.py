class DLLIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        current_data = self.current.item
        self.current = self.current.next
        return current_data


# Que:-1
class Node:
    def __init__(self, item=None, prev=None, next_ref=None):
        self.prev = prev
        self.item = item
        self.next = next_ref


# Que:-2
class DLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    # Que:-3
    def is_empty(self):
        return self.start is None

    # Que:-4
    def insert_at_start(self, data):
        new_node_object = Node(data)
        new_node_object.next = self.start
        if not self.is_empty():
            self.start.prev = new_node_object
        self.start = new_node_object
        # increment the value of counter
        self.count += 1

    # Que:-5
    def insert_at_last(self, data):
        new_node_object = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            # Last Node reference
            new_node_object.prev = temp
            temp.next = new_node_object
        else:
            self.start = new_node_object
        # increment the value of counter
        self.count += 1

    # Que:-6
    def search(self, search_data):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                if temp.item == search_data:
                    return True
                temp = temp.next
            # To check last Node data with search_data
            if temp.item == search_data:
                return True
            return False
        else:
            return "DLL is empty."

    # Que:-7
    def printList(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)
        else:
            return "DLL is empty."

    # Que:-8
    def insert_after(self, search_data, insert_data):
        if not self.is_empty() and self.search(search_data):
            new_node_object = Node(insert_data)
            temp = self.start
            while temp.next is not None:
                if temp.item == search_data:
                    new_node_object.prev = temp.next.prev
                    new_node_object.next = temp.next
                    temp.next = new_node_object
                    temp.next.prev = new_node_object
                    break
                temp = temp.next
            else:
                # To insert data after the last Node If value is match.
                if temp.next is None:
                    new_node_object.prev = temp
                    new_node_object.next = None
                    temp.next = new_node_object
            # Increment the value of counter
            self.count += 1
        else:
            return "DLL is empty."

    # Que:-9
    def delete_first(self):
        if not self.is_empty():
            # If DLL contains only one Node, then do this.
            if self.start.next is None:
                self.start = None
            # If DLL contains at least two Node then do this.
            else:
                self.start.next.prev = None
                self.start = self.start.next
            # decrement the value of counter
            self.count -= 1
        else:
            return "DLL is empty."

    # Que:-10
    def delete_last(self):
        if not self.is_empty():
            # If DLL contains only one Node, then do this.
            if self.start.next is None:
                self.start = None
            # If DLL contains at least two Node then do this.
            else:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None
            # increment the value of counter
            self.count -= 1
        else:
            return "DLL is empty."

    # Que:-11
    def delete_item(self, search_data):
        if not self.is_empty() and self.search(search_data):
            temp = self.start
            # If DLL contains only one Node, then do this.
            if temp.next is None:
                self.start = None
            # If DLL contains more than one Node, then do this.
            else:
                # If DLL contains more than one Node, and we have to
                # delete first Node then do this.
                if temp.item == search_data:
                    self.start.next.prev = None
                    self.start = self.start.next
                # To Delete another Node, then do this.
                else:
                    while temp.next is not None:
                        if temp.next.item == search_data:
                            # To Handle the Last Node.
                            if temp.next.next is not None:
                                temp.next.next.prev = temp
                            temp.next = temp.next.next
                            break
                        temp = temp.next
            # Decrement the value of counter.
            self.count -= 1
        else:
            return "DLL is empty or search data not in linked list."

    # This is an optimize method to remove a particular item.
    def remove_item(self, search_data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == search_data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    # Decrement the value of counter.
                    self.count -= 1
                temp = temp.next

        else:
            return "DLL is empty."

    # Que:-12
    def __iter__(self):
        return DLLIterator(self.start)

    def length(self):
        return self.count


# --------------------Testing code---------------
myList = DLL()
print("List is empty or not:", myList.is_empty())
myList.insert_at_start(40)
myList.insert_at_start(20)
myList.insert_at_last(60)
# print()
myList.insert_at_last(80)
# myList.insert_at_last(80)
# myList.insert_at_last(500)
myList.printList()
# print("\nAfter delete DLL is :")
# myList.delete_first()
# myList.delete_last()
# myList.delete_item(60)
# myList.delete_item(40)
# myList.delete_item(100)
# myList.insert_after(80, 90)
myList.remove_item(80)
print("After operation")
myList.printList()
print()
# print(f"Search data is {500} :", myList.search(500))
print("Length of DLL is :", myList.length())
print("List is empty or not:", myList.is_empty())
print("For Loop operation: ")
for item in myList:
    print(item, end=" ")
