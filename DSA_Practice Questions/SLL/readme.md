# SLL (Singly Linked List) :- 

- **SLL is a linear data structure.** 
- **It can grow and shrink.**

### <ins>Basic Operation on SLL :- </ins>
1. Insertion
2. Deletion
3. is_empty
4. traversing
----------------
* ### <ins>Basic Practice Problems On Singly Linked List :- </ins>

1. Define a class Node to describe a node of singly linked list.
2. Define a class SLL to with `__init__()` method to create and initialize start reference variable.
3. Define a method `is_empty()` to class if the linked list is empty in SLL class.
4. In class SLL define a method `insert_at_start()` to insert an element at the starting of the list.
5. In class SLL define a method `insert_at_last()` to insert an element at the end of the list.
6. In a class SLL define a method to `search()` to find the node with specified element value.
7. In a class SLL define a method `insert_after()` to insert a new node after a given node of the list.
8. In a class SLL define  `printList()` method to print all elements of the list.
9. In a class SLL define a method `delete_first()` to delete a first element of the list in a sequence.
10. In a class SLL define a method `delete_last()` to delete last element from the list.
11. In a class SLL define a method `delete_item()` to delete a specified element from the list.
12. In a class SLL implement `iterator` for SLL to access all the elements of the list in a sequence.

-----------




>[! Important] -
> How to make a Singly Linked List is iterable: -

- First, We create an Iterator class after creating an Iterator class we create an object of that class in which that 
class we want to make an Iterable. 
```python

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
```

- Make an object.
```python
class SLL:
    def __init__(self, start=None):
        self.start = start
    # To make an object of SLLIterator.
    def __iter__(self):
        return SLLIterator(self.start)
```
