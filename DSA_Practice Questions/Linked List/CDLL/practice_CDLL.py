class Node:
    def __init__(self, item=None, prev=None, next_ref=None):
        self.prev = prev
        self.item = item
        self.next = next_ref


class CDLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.is_empty():
            new_node.prev = self.start.prev
            new_node.next = self.start

            self.start.prev.next = new_node
            self.start.prev = new_node

        else:
            new_node.prev = new_node
            new_node.next = new_node

        self.start = new_node

        # increment the value of counter.
        self.count += 1

    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.is_empty():
            new_node.prev = self.start.prev
            new_node.next = self.start

            self.start.prev.next = new_node
            self.start.prev = new_node

        else:
            new_node.prev = new_node
            new_node.next = new_node

            self.start = new_node

        # increment the value of counter.
        self.count += 1

    def insert_after(self, search_data, insert_data):
        if not self.is_empty():
            if self.search_element(search_data):
                new_node = Node(insert_data)

                temp = self.start
                while temp.next is not self.start:
                    if temp.item == search_data:
                        new_node.prev = temp
                        new_node.next = temp.next

                        temp.next.prev = new_node
                        temp.next = new_node

                    temp = temp.next

                if temp.item == search_data:
                    new_node.prev = temp
                    new_node.next = self.start

                    self.start.prev = new_node
                    temp.next = new_node

                # increment the value of counter
                self.count += 1
            else:
                raise ValueError(f"element {search_data} is not in CDLL.")

            pass
        else:
            raise ValueError("CDLL is empty.")

    def print_list(self):
        if not self.is_empty():
            temp = self.start

            while temp.next != self.start:
                print(temp.item, end=" ")
                temp = temp.next

            # To print last node item value
            print(temp.item)
        else:
            print("list is empty.")
            # raise ValueError("CDLL is empty.")
        pass

    def search_element(self, search_data):
        if not self.is_empty():
            temp = self.start
            while temp.next is not self.start:
                if temp.item == search_data:
                    return True
                temp = temp.next

            # To check last node data
            if temp.item == search_data:
                return True
            return False

        else:
            raise ValueError("CDLL is empty.")

    def delete_start(self):
        if not self.is_empty():
            temp = self.start

            # if CDLL contains only one Node then do this.
            if temp.prev == self.start:
                self.start = None
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next

                self.start = self.start.next

            # decrease the value of counter
            self.count -= 1

        else:
            raise ValueError("CDLL is empty.")
        pass

    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            if temp.next == self.start:
                self.start = None
            else:
                while temp.next is not self.start:
                    temp = temp.next

                temp.prev.next = self.start
                self.start.prev = temp.prev

            # decrease the value of counter
            self.count -= 1
        else:
            raise ValueError("CDLL is empty.")
        pass

    def delete_item(self, delete_element):
        if not self.is_empty():
            if self.search_element(delete_element):

                temp = self.start

                # if CDLL contains one Node then do this
                if temp.next == self.start and temp.item == delete_element:
                    self.start = None

                else:
                    # To delete first Node
                    if temp.item == delete_element:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                        self.start = temp.next

                    else:

                        while temp.next is not self.start:
                            if temp.item == delete_element:
                                temp.prev.next = temp.next
                                temp.next.prev = temp.prev
                                break
                            temp = temp.next

                        # To delete last node then do this
                        if temp.item == delete_element:
                            temp.prev.next = temp.next
                            temp.next.prev = temp.prev
                            pass

            else:
                raise ValueError(f"Element {delete_element} is not in the CDLL.")
            pass
            # decrement the value of counter
            self.count -= 1
        else:
            raise ValueError("CDLL is empty.")

    def length(self):
        return self.count


# -------------------------- Testing Code ------------------------------
my_list = CDLL()
print("List is empty or not::", my_list.is_empty())
my_list.insert_at_start(80)
my_list.insert_at_start(60)
# my_list.insert_at_start(40)
my_list.insert_at_start(20)
my_list.insert_at_last(100)
my_list.print_list()

print("*" * 60)
# my_list.insert_after(80, 101)
print("after deleting ")
# print("after inserting")
# my_list.delete_start()
# my_list.delete_start()
# my_list.delete_start()
# my_list.delete_start()
# my_list.delete_start()
# ---------------
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()

# ---------------
my_list.delete_item(80)
# my_list.delete_item(101)
my_list.delete_item(100)
my_list.delete_item(20)
my_list.delete_item(60)

my_list.print_list()

# user_input = int(input("enter the element that you want to search:: "))
# print(f"element {user_input} is in the list :", my_list.search_element(user_input))
print("length of list::", my_list.length())
print("List is empty or not::", my_list.is_empty())
