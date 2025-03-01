# Que:-1

class Node:
    def __init__(self, item=None, next_item=None):
        self.item = item
        self.next = next_item


class SLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    # 🥰
    def insert_at_start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data, None)
        if self.is_empty():
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # 🥰
    def delete_first(self):
        if not self.is_empty():
            # print('this is self.start.next-', self.start.next)
            self.start = self.start.next

        else:
            raise ValueError("SLL is empty.")

    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            # if SLL contains only one item then
            if self.start.next is None:
                self.start = None
            # if SLL contains at least 2 Nodes then do this
            else:
                while temp.next.next is not None:
                    temp = temp.next

                temp.next = None
            # if SLL contains only one elements then do this.

        else:
            raise ValueError("SLL is empty.")

    def print_elements(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                print(temp.item, end=" ")
                temp = temp.next
            else:
                print(temp.item)

        else:
            print("Linked List is empty.")


# ------------------------------- Testing code

item = SLL()
print("Linked list is empty  ::", item.is_empty())
item.insert_at_start(60)
item.insert_at_start(40)
item.insert_at_start(20)
#
# item.insert_at_last(80)
item.insert_at_last(100)
# item.insert_at_last(120)

item.print_elements()
# -------------------- delete
# item.delete_last()

# item.delete_first()
# item.delete_first()
# item.delete_first()
# item.delete_first()

print()
item.print_elements()

print("Linked list is empty  ::", item.is_empty())
