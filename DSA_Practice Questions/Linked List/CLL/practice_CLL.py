class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref


class CLL:
    def __init__(self, last=None):
        self.last = last
        self.count = 0

    def is_empty(self):
        return self.last is None

    # 🥰
    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.last.next
            self.last.next = new_node
        else:
            new_node.next = new_node
            self.last = new_node

        # increment the value of counter
        self.count += 1

    # 🥰
    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.last.next
            self.last.next = new_node
        else:
            new_node.next = new_node

        self.last = new_node

        # increment the value of counter
        self.count += 1

    # 🥰
    def insert_after(self, search_data, insert_data):
        if not self.is_empty():
            if self.search_element(search_data):
                new_node = Node(insert_data)

                # get first node reference
                temp = self.last.next
                while temp.next is not self.last.next:
                    if temp.item == search_data:
                        new_node.next = temp.next
                        temp.next = new_node

                        # increment the value of counter
                        self.count += 1

                        break
                    temp = temp.next

                # To insert data after last node
                else:
                    if temp.item == search_data:
                        new_node.next = temp.next
                        temp.next = new_node
                        self.last = new_node

                        # increment the value of counter
                        self.count += 1

            else:
                raise ValueError(f"element {search_data} is not in the CLL.")

        else:
            return ValueError("CLL is empty.")

    # 🥰
    def search_element(self, search_data):
        if not self.is_empty():
            # get first node reference
            temp = self.last.next
            while temp.next != self.last.next:
                if temp.item == search_data:
                    return True
                temp = temp.next

            # To check last node
            else:
                if temp.item == search_data:
                    return True
                else:
                    return False

        else:
            return ValueError("CLL is empty.")

    # 🥰
    def print_list(self):
        if not self.is_empty():

            # get reference of first Node
            temp = self.last.next
            while temp.next != self.last.next:
                print(temp.item, end=" ")
                temp = temp.next

            # To print last Node data
            print(temp.item, end=" ")
        else:
            print("CLL is empty.")
        pass

    def delete_start(self):
        if not self.is_empty():
            # 🤔 TODO think again

            # if CLL consist only one node then do this.
            if self.last.next.next == self.last.next:
                # print("if list consist only one node then do this.")
                self.last = None

            # if CLL consist more than one node then do this.
            else:
                self.last.next = self.last.next.next

            # decrement the value of counter
            self.count -= 1

        else:
            raise ValueError("CLL is empty.")

    def delete_last(self):
        if not self.is_empty():
            temp = self.last.next
            if temp.next == self.last.next:
                self.last = None
                pass
            else:
                # if list contains more than one node then do this
                while temp.next.next is not self.last.next:
                    temp = temp.next

                temp.next = self.last.next
                self.last = temp

            # decrement the value of counter
            self.count -= 1
        else:
            raise ValueError("CLL is empty.")
        pass

    # TODO to fix this method minimum two element then
    def delete_item(self, delete_item):
        if not self.is_empty():
            temp = self.last.next

            # if list contains only one Node then do this.
            if temp.next == temp:
                print("if only one item")
                self.last = None

            else:
                while temp.next is not self.last.next:
                    if temp.next.item == delete_item:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

        else:
            raise ValueError("CLL is empty.")
        pass

    def delete_after(self, search_item):
        if not self.is_empty():
            temp = self.last.next
            while temp.next is not self.last.next:
                if temp.item == search_item:
                    temp.next = temp.next.next
                    break
                temp = temp.next

            self.count -= 1
        else:
            raise ValueError("CLL is empty.")
        pass

    def length(self):
        return self.count

    def __iter__(self):
        if self.last is None:
            return CLLIterator(self.last)
        else:
            return CLLIterator(self.last.next)


class CLLIterator:
    def __init__(self, current):
        self.current = current

        # get the reference of first node
        self.first = current
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        # if list is empty then do this.
        if not self.current:
            raise StopIteration

        if self.current == self.first and self.count == 1:
            raise StopIteration
        else:
            self.count = 1

        current_data = self.current.item
        self.current = self.current.next

        return current_data


# ------------------------- Testing Code ---------------------------
my_list = CLL()
print("CLL is empty or not::", my_list.is_empty())
# my_list.insert_at_start(60)
# my_list.insert_at_start(40)
my_list.insert_at_last(80)
my_list.insert_at_last(100)
# my_list.print_list()
print()
# user_search_value = int(input("enter the value that you want to search:: "))
# user_input_value = int(input("enter the value that you want to search:: "))

# print(f"element {user_input} is in the CLL :: {my_list.search_element(user_input)}")

print("*" * 60)
my_list.insert_after(100, 500)
my_list.insert_after(80, 900)
my_list.print_list()
# my_list.insert_after(user_search_value, user_input_value)


# my_list.insert_after(60, 500)
# my_list.insert_after(500, 1000)
# my_list.delete_start()
# my_list.delete_start()
# my_list.delete_start()
# my_list.delete_start()
# my_list.delete_after(900)
print("\nafter delete element CLL.")
# my_list.delete_item()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_after(900)
# my_list.delete_after(900)
# my_list.delete_after(900)
my_list.delete_item(100)
my_list.delete_item(500)
# my_list.delete_item(900)
my_list.delete_item(80)
# my_list.delete_item(900)
# my_list.delete_after(80)
my_list.print_list()

# my_list.print_list()
print()

print("Total No. of item in CLL::", my_list.length())
# print("CLL is empty or not::", my_list.is_empty())
