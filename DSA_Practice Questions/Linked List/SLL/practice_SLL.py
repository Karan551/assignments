# IMP: head---> start (both are same)

# Que:-1

class Node:
    def __init__(self, item=None, next_item=None):
        self.item = item
        self.next = next_item


class SLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    # 🥰
    def insert_at_start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node
        self.count += 1

    def insert_at_last(self, data):
        new_node = Node(data, None)
        if self.is_empty():
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

        # increase the value of counter
        self.count += 1

    def insert_after(self, search_data, insert_data):
        if not self.is_empty():
            if self.search(search_data):
                temp = self.start

                new_node = Node(insert_data)

                while temp is not None:
                    if temp.item == search_data:
                        new_node.next = temp.next
                        temp.next = new_node
                    temp = temp.next
            else:
                raise ValueError("Value not in the SLL.")
        else:
            raise ValueError("SLL is empty.")

    # 🥰
    def delete_first(self):
        if not self.is_empty():
            # print('this is self.start.next-', self.start.next)
            self.start = self.start.next

            # decrease the value of counter
            self.count -= 1

        else:
            raise ValueError("SLL is empty.")

    def delete_last(self):
        if not self.is_empty():

            # decrease the value of counter
            self.count -= 1

            temp = self.start
            # if SLL contains only one item then
            if self.start.next is None:
                self.start = None

            # if SLL contains at least 2 Nodes then do this
            else:
                while temp.next.next is not None:
                    temp = temp.next

                temp.next = None

        else:
            raise ValueError("SLL is empty.")

    def delete_item(self, element):
        if not self.is_empty():

            if self.search(element):
                temp = self.start

                # if SLL contains only single Node
                if temp.next is None:
                    self.start = None

                else:
                    # if we want to delete first Node then do this
                    if temp.item == element:
                        self.start = temp.next
                    else:
                        while temp.next is not None:
                            if temp.next.item == element:
                                temp.next = temp.next.next
                                break
                            temp = temp.next

                # decrement the value of counter
                self.count -= 1
            else:
                raise ValueError("Value is not exist in SLL.")
        else:
            raise ValueError("SLL is empty.")

    # TODO: fix this code
    def delete_after(self, element):
        if not self.is_empty():
            if self.search(element):
                temp = self.start

                # if SLL contains only one Node then do this
                if temp.next is None:
                    return None

                # if we want to delete 2nd Node and SLL contains maximum 2 Nodes.
                elif temp.next.item == element and temp.next.next is None:
                    temp.next = None

                # if SLL contains minimum 2 Nodes then.
                else:
                    while temp.next.next is None:
                        if temp.next.next.item == element:
                            temp.next.next = temp.next.next.next
                            pass
                    pass
            else:
                raise ValueError("Value does not exist in SLL.")
            pass
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

    def length(self):
        return self.count

    def __iter__(self):
        return SLLIterator(self.start)

    # 🥰
    def search(self, data):
        if not self.is_empty():
            temp = self.start

            while temp is not None:
                if temp.item == data:
                    return True
                temp = temp.next
            else:
                return False

        else:
            raise ValueError("SLL is empty.")


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

print("Linked list is empty  ::", item.is_empty())
print("total elements in SLL is ::", item.length())
# user_check = int(input("enter the value that you want to check:: "))
# user_input = int(input("enter the value that you want to delete:: "))

# item.insert_after(user_check, user_input)


# item.delete_item(20)
item.delete_item(40)
item.delete_item(100)
item.delete_item(60)
item.delete_item(20)
print("*" * 60)
print("after deleting")
print("Length of SLL:", item.length())
item.print_elements()
# print("search result::", item.search(user_input))
# for i in item:
#     print(i, end=" ")
print("this is class name", item.__class__.__name__)
