class Node:
    def __init__(self, item=None, nex_ref=None):
        self.item = item
        self.next = nex_ref


class CLL:
    def __init__(self, last=None):
        self.last = last
        self.count = 0

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, data):
        new_node_object = Node(data)
        if not self.is_empty():
            new_node_object.next = self.last.next
            self.last.next = new_node_object
        # If a list is empty, then do this.
        else:
            new_node_object.next = new_node_object
            self.last = new_node_object
        # Increment the value of counter
        self.count += 1

    def insert_at_last(self, data):
        new_node_object = Node(data)
        if not self.is_empty():
            new_node_object.next = self.last.next
            self.last.next = new_node_object
        else:
            new_node_object.next = new_node_object
        self.last = new_node_object
        # Increment the value of counter
        self.count += 1

    def search(self, search_data):
        if not self.is_empty():
            temp = self.last.next
            while temp.next is not self.last.next:
                if temp.item == search_data:
                    return True
                temp = temp.next
            # To check last Node data with search_data.
            if temp.item == search_data:
                return True
            else:
                return False

    def insert_after(self, search_data, insert_data):
        if not self.is_empty() and self.search(search_data):
            temp = self.last.next
            new_node_object = Node(insert_data)
            # If insert_after first Node and list contains only
            # one Node, then do this.
            if temp.next == temp:
                new_node_object.next = temp
                temp.next = new_node_object
                self.last = new_node_object
            # If insert_after first Node and list
            # contains at least two Node then do this.
            elif temp.item == search_data:
                new_node_object.next = temp.next
                temp.next = new_node_object
            else:
                while temp.next is not self.last.next:
                    if temp.item == search_data and temp.next != self.last.next:
                        new_node_object.next = temp.next
                        temp.next = new_node_object
                        break
                    temp = temp.next
                if temp.item == search_data and temp.next == self.last.next:
                    new_node_object.next = temp.next
                    temp.next = new_node_object
                    self.last = new_node_object
                # Increment the value of counter
                self.count += 1

            pass
        else:
            return "CLL is empty."

    def printList(self):
        if not self.is_empty():
            # Get First Node reference
            temp = self.last.next
            while temp.next is not self.last.next:
                print(temp.item, end=" ")
                temp = temp.next
            # To print last Node data
            print(temp.item)
        else:
            return "CLL is empty."

    def delete_start(self):
        if not self.is_empty():
            temp = self.last.next
            # If CLL contains only one Node, then do this.
            if temp.next == temp:
                self.last = None
            else:
                self.last.next = temp.next
            # Decrement the value of counter
            self.count -= 1
        else:
            return "CLL is empty."

    def delete_last(self):
        if not self.is_empty():
            temp = self.last.next
            if temp.next == temp:
                self.last = None
            else:
                while temp.next.next is not self.last.next:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
            # Decrement the value of counter.
            self.count -= 1
        else:
            return "CLL is empty."

    def delete_item(self, search_data):
        if not self.is_empty() and self.search(search_data):
            temp = self.last.next
            # If CLL contains only one Node, then do this.
            if temp.next == temp:
                self.last = None
            # If CLL contains at least two Node and deletes first Node.
            else:
                if temp.item == search_data:
                    self.last.next = temp.next
                # To Delete another Node in CLL.
                else:
                    while temp.next is not self.last.next:
                        if temp.next.item == search_data:
                            temp.next = temp.next.next
                        temp = temp.next
            # Decrement the value of counter.
            self.count -= 1
        else:
            return "CLL is empty."

    def length(self):
        return self.count


# ------------------Testing Code---------
myList = CLL()
print("List is empty or not:", myList.is_empty())
# myList.insert_at_start(60)
myList.insert_at_start(40)
myList.insert_at_start(20)
myList.insert_at_last(60)
myList.insert_at_last(80)
myList.printList()
print("After deletion")
myList.delete_item(80)
# myList.delete_start()
# myList.delete_last()

# myList.insert_after(40, 50)
myList.printList()

# print()
# print(f"List contains {60} :", myList.search(60))
print("List is empty or not:", myList.is_empty())
print("List length is :", myList.length())
