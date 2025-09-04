class Node:
    def __init__(self, prev_ref=None, item=None, next_ref=None):
        self.prev = prev_ref
        self.item = item
        self.next = next_ref


class DLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    # 🥰
    def insert_at_start(self, data):
        new_node = Node(None, data, self.start)

        if not self.is_empty():
            self.start.prev = new_node

        self.start = new_node

        # increase the value of counter.
        self.count += 1

    def insert_at_last(self, data):
        if not self.is_empty():
            temp = self.start

            while temp.next is not None:
                temp = temp.next

            new_node = Node(temp, data, None)
            temp.next = new_node

        else:
            new_node = Node(None, data)
            self.start = new_node

        # increase the value of counter
        self.count += 1

    def insert_after(self, search_data, insert_data):
        if not self.is_empty():
            if self.search_item(search_data):
                temp = self.start
                while temp is not None:
                    if temp.item == search_data:
                        new_node = Node(temp, insert_data, temp.next)
                        if temp.next is not None:
                            temp.next.prev = new_node
                        temp.next = new_node

                        # increase the value of counter
                        self.count += 1

                        break
                    temp = temp.next

                pass
            else:
                raise ValueError(f"Element {search_data} doesn't exist in DLL.")
            pass
        else:
            raise ValueError("DLL is empty.")
        pass

    def search_item(self, data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return True

                temp = temp.next
            else:
                return False

        else:
            raise ValueError("DLL is empty.")

    # 🥰
    def delete_first(self):
        if not self.is_empty():
            if self.start.next is not None:
                self.start.next.prev = None
            self.start = self.start.next

            # decrease the value of counter
            self.count -= 1
        else:
            raise ValueError("DLL is empty.")

    # 🥰
    def delete_last(self):
        if not self.is_empty():
            temp = self.start
            if temp.next is None and temp.prev is None:
                self.start = None

            else:
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None

            # decrease the value of counter.
            self.count -= 1
        else:
            raise ValueError("DLL is empty.")
        pass

    def delete_item(self, delete_data):
        if not self.is_empty():
            if self.search_item(delete_data):
                if self.start.prev is None and self.start.next is None and self.start.item == delete_data:
                    self.start = None

                else:
                    temp = self.start
                    while temp.next is not None:
                        if temp.item == delete_data:
                            if temp.next is not None:
                                temp.next.prev = temp.prev

                            if temp.prev is not None:
                                temp.prev.next = temp.next

                            # To delete first element in the DLL.
                            if temp.prev is None:
                                temp.next.prev = None
                                self.start = temp.next

                        temp = temp.next

                    if temp.next is None:
                        temp.prev.next = None

            else:
                raise ValueError(f"Element {delete_data} is not exist in the DLL.")

        else:
            raise ValueError("DLL is empty.")
        pass

    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
        else:
            print("DLL is empty.")

    def length(self):
        return self.count

    def __iter__(self):
        return DLLIterator(self.start)

    # def __str__(self):
    #     return f"Node value {self.item}"
    #     print("this is node item")


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


# ------------------------------- Testing code---------------------

my_list = DLL()
print("DLL is empty or not::", my_list.is_empty())

# my_list.insert_at_start(60)
# my_list.insert_at_start(20)
# my_list.insert_at_start(40)

print("elements in DLL::", my_list.length())
# my_list.print_list()
my_list.insert_at_last(80)
my_list.insert_at_last(6000)
my_list.insert_at_last(200)
my_list.insert_at_last(700)
my_list.insert_at_start(20)
# my_list.insert_at_start(100)
# my_list.insert_at_start(250)
print()
for i in my_list:
    print(i, end=" ")
print()
# my_list.delete_first()
# my_list.delete_first()
# my_list.delete_first()
# my_list.delete_first()
print()
print("*" * 60)

print("elements in DLL::", my_list.length())
# my_list.print_list()
# print("DLL is empty or not::", my_list.is_empty())
# user_input = int(input("enter the element that you want to search : "))
# print(f"\n{user_input} element in the list :", my_list.search_item(user_input))
# my_list.insert_after(user_input, 51)
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
print("after delete")
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()
# my_list.delete_last()

my_list.delete_item(700)

my_list.print_list()
print("\nlength of the DLL:", my_list.length())
