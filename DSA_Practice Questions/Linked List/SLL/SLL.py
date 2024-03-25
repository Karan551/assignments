# Que-1
class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class SLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_node_object = Node(data, self.start)
        self.start = new_node_object
        self.count += 1

    def insert_at_last(self, data):
        new_node_object = Node(data)
        # If List contains no item then do this.
        if self.is_empty():
            self.start = new_node_object
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node_object
        # To increment the value of counter.
        self.count += 1

    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                print(temp.item, end=" ")
                temp = temp.next
            # To print the last item
            print(temp.item)
        else:
            print("List is empty.")

    def search(self, search_data):
        temp = self.start
        while temp.next is not None:
            if temp.item == search_data:
                return True
            temp = temp.next
        # To check the last item in the list.
        if temp.item == search_data:
            return True
        else:
            return False

    def item_count(self):
        return self.count

    def delete_first(self):
        if not self.is_empty():
            # if list contains only one item.
            if self.start.next is None:
                self.start = None
            else:
                self.start = self.start.next
            self.count -= 1


# -----------------Testing Code---------
myList = SLL()
print("List is empty :", myList.is_empty())
myList.insert_at_start(20)
myList.insert_at_start(60)
myList.insert_at_start(100)
# myList.insert_at_start(10)
myList.print_list()
print("Total Number of elements in SLL", myList.item_count())
myList.delete_first()
myList.delete_first()
myList.delete_first()
# myList.insert_at_last(50)
print("List is empty :", myList.is_empty())
# myList.insert_at_last(500)
myList.print_list()
print("Total Number of elements in SLL", myList.item_count())

# print("List contains 51 :", myList.search(20))
# print("List contains 5000 :", myList.search(5000))
