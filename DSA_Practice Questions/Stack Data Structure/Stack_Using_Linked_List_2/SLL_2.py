class SLLIterator:
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
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class SLL:
    # Que:-2
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    # Que:-3
    def is_empty(self):
        return self.start is None

    # Que:-4
    def insert_at_start(self, insert_data):
        node_object = Node(insert_data, self.start)
        self.start = node_object
        self.count += 1

    # Que:-5
    def insert_last(self, insert_data):
        node_object = Node(insert_data)
        if self.is_empty():
            self.start = node_object
        else:
            # To get the reference of first Node.
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node_object
        # Increment the value of counter.
        self.count += 1

    # Que:-6
    def search(self, search_data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == search_data:
                    return True
                temp = temp.next
            else:
                return False

    # Que:-7
    def insert_after(self, search_data, insert_data):
        if not self.is_empty() and self.search(search_data):
            node_object = Node(insert_data)
            temp = self.start
            while temp.next is not None:
                if temp.item == search_data:
                    node_object.next = temp.next
                    temp.next = node_object
                temp = temp.next
            temp.next = node_object
            # Increment the value of counter.
            self.count += 1
        else:
            return "SLL is empty."

    # Que:-8
    def printList(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
        else:
            print("SLL is empty.")

    # Que:-9
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
            # Decrement the value of counter.
            self.count -= 1
        else:
            return "SLL is empty."

    # Que:-10
    def delete_last(self):
        if not self.is_empty():
            # ---- 1) First when SLL contains only one Node
            if self.start.next is None:
                self.start = None
            # ---- 2) Second when SLL contains at least two Nodes.
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
            # Decrement the value of counter.
            self.count -= 1

    # Que:-11
    def delete_item(self, delete_data):
        if not self.is_empty() and self.search(delete_data):
            # When SLL contains only one Node, then do this.
            if self.start.next is None:
                self.start = None
            # When SLL contains at least two Node then do this.
            else:
                temp = self.start
                # If SLL contains at least two Node, and we want to
                # delete first Node then do this.
                if temp.item == delete_data:
                    self.start = self.start.next
                # If we want to delete another Node item, then do this.
                else:
                    while temp.next is not None:
                        # we compare next node item with delete_data.
                        if temp.next.item == delete_data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next
                    else:
                        return None
                # Decrement the value of counter.
                self.count -= 1
        else:
            return "SLL is empty."

    def del_after(self, search_data):
        if not self.is_empty() and self.search(search_data):
            # ---- 1) When delete data after first Node
            if self.start.item == search_data:
                # ---- If SLL contains only one Node, then do this.
                if self.start.next is None:
                    return False
                else:
                    self.start.next = self.start.next.next
            else:
                temp = self.start
                while temp.next is not None:
                    if temp.item == search_data:
                        if temp.next.next is not None:
                            temp.next = temp.next.next
                        else:
                            temp.next = None
                    temp = temp.next
                # print("This is last item ", temp.item)
        else:
            return None

    # Que:12
    def __iter__(self):
        return SLLIterator(self.start)

    def length(self):
        return self.count


# ------------------Testing code------------
if __name__ == "__main__":
    myList = SLL()
    print("List is empty or not :", myList.is_empty())
    # myList.insert_at_start(20)
    myList.insert_at_start(80)
    myList.insert_at_start(60)
    myList.insert_at_start(40)
    myList.insert_at_start(20)
    # myList.insert_at_start(90)
    # myList.insert_last(100)
    myList.printList()
    print()
    myList.insert_after(80, 70)
    # print(f"List contains {1001} or not-", myList.search(1001))
    # myList.del_after(60)
    print("After inserting SLL is:")
    # myList.delete_first()
    # myList.delete_last()
    # myList.delete_item(80)
    # myList.delete_item(40)
    # myList.delete_item(20)

    # print("After Deleting one item SLL Is :")
    myList.printList()
    # print("\nList is empty or not :", myList.is_empty())
    print("\nThe size of the SLL is:", myList.length())
    for data in myList:
        print(data, end=" ")
