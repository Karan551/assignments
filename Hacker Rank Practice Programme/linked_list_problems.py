# IMP: head---> start (both are same)
# IMP: head---> self.start
# temp(head) = self.start
# data, head

# while temp is not None:
#     print(temp.item)
#     temp = temp.next

lst = [1, 4, 6, 76, 90, 87]


# print(lst[::-1])
# for i in lst[::-1]:
#     print(i)


# --------------------------
class SinglyLinkedlistNode:
    def __init__(self, item, next_ref):
        self.data = item
        self.next_ref = next_ref


class SLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def insert_node_at_start(self, data):
        new_node = SinglyLinkedlistNode(data)
        # new_node.next_ref=


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


x = Person("Ganesh", 21)
print(x)
print(hasattr(x, "age"))
print(hasattr(x, "get_age"))
print(x.__class__.__name__)
