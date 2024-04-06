class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class SLL:
    def __init__(self, start=None):
        self.start = None
        self.count = 0

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_node_object = Node(data, self.start)
        self.start = new_node_object
        self.count += 1

    def printList(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next

    def return_list(self):
        if not self.is_empty():
            lst = []
            temp = self.start
            while temp is not None:
                lst.append(temp.item)
                temp = temp.next
            return lst

    def middle_node(self):
        if not self.is_empty():
            lst = self.return_list()
            length = len(lst)
            return lst[length // 2] if length % 2 != 0 else (lst[length // 2 - 1], lst[length // 2])

    def reverse_list(self):
        return self.return_list()[::-1]

    def delete_middle(self):
        if self.is_empty():
            return None
        if self.count % 2 != 0:
            i = 1
            del_node_count = self.count // 2
            temp = self.start
            while temp is not None:
                if del_node_count == i:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                i += 1
        else:
            # ye fix karna hai..
            i = 1
            del_node_count = self.count // 2
            temp = self.start
            while temp is not None:
                if del_node_count == i:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                i += 1


# -------------Testing Code-------------
myList = SLL()
print("List Is empty:", myList.is_empty())
# myList.insert_at_start(120)
myList.insert_at_start(100)
myList.insert_at_start(80)
myList.insert_at_start(60)
myList.insert_at_start(40)
myList.insert_at_start(20)
myList.insert_at_start(10)
# myList.insert_at_start(5)
myList.printList()
print()
myList.delete_middle()
myList.printList()
print()
# print(myList.middle_node())
# print(type(myList.middle_node()))
# print("reverse list")
# print(myList.reverse_list())
print("List Is empty:", myList.is_empty())
