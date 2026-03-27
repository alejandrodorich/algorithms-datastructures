from typing import Any

class Node:
    """Node of a doubly linked list."""

    def __init__(self, entry):
        self.entry = entry
        self.next = None
        self.previous = None

class DoublyLinkedList:


    def __init__(self):
        ''' Initialize a new empty doubly linked list.'''
        self.head = None
        self.tail = None
        self.size = 0


    def __iter__(self):
        ''' Make the doubly linked list iterable.'''
        current_node = self.head
        while current_node is not None:
            yield current_node.entry
            current_node = current_node.next


    def __len__(self) -> int:
        ''' Make length function work on doubly linked list. 
            
            Returns:
                int: Size of the doubly linked list.

        '''
        return self.size
    

    def get(self,index : int) -> Any:
        ''' Get the value at the specified index in the doubly linked list.
        
            Args:
                index (int): The index of the value to be returned.
            
            Returns:
                Any: The value at the specified index.
            
            Raises:
                IndexError: If the index is out of bounds.
            '''

        # check if index is out of bounds
        if index >= self.size or index < 0:
            raise IndexError("Index out of bounds")

        # traverse the doubly linked list to the specified index
        current_node = self.head
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        
        return current_node.entry
    

    def index_of(self, value) -> int:
        ''' Get the index of the given value in the doubly linked list.
            
            Args:
                value: Value to be searched. Must support equality comparison.
            
            Returns:
                int: The index of the given value in the doubly linked list.

            Raises:
                ValueError: If value is not contained in the doubly linked list.
        '''
        
        # traverse the doubly linked list to the given value
        current_node = self.head
        current_index = 0
        while current_node is not None and current_node.entry != value:
            current_index += 1
            current_node = current_node.next

        if current_node is None:
            raise ValueError("Value is not contained in list")
        return current_index
    
  
    def pop(self) -> Any:
        ''' Deletes the last element in the doubly linked list.

            Returns:
                Any: The deleted value.
         
            Raises:
                IndexError: If the doubly linked list is empty.
        '''
        
        if self.size == 0:
            raise IndexError("List is Empty")
        
        popped_value = self.tail.entry
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            new_ending = self.tail.previous
            new_ending.next = None
            self.tail = new_ending
        self.size -= 1

        return popped_value
    

    def delete(self, value) -> None:
        ''' Deletes the first occurrence of the element in the doubly linked list.
        
            Args:
                value: Value to be deleted.
            
            Raises:
                ValueError: Value is not contained in list.
        '''

        if self.head is None:
            raise ValueError("List is empty")

        current_node = self.head
        while current_node is not None and current_node.entry != value:
            current_node = current_node.next

        if current_node is None:
            raise ValueError("Value is not contained in list.")
        
        previous_node = current_node.previous
        next_node = current_node.next

        # reconnect previous node or update head if deleting the first node
        if previous_node is None:
            self.head = next_node
        else:
            previous_node.next = next_node

        # reconnect next node or update tail if deleting the last node
        if next_node is None:
            self.tail = previous_node
        else:
            next_node.previous = previous_node

        self.size -= 1

    def contains(self, value) -> bool:
        ''' Searches for a given value in the doubly linked list.

            Args:
                value: Value to be searched. Must support equality comparison.
            
            Returns:
                bool: True if value is contained in the doubly linked list, False otherwise. 
        
        '''
        current_node = self.head
        while current_node is not None:
            if current_node.entry == value:
                return True
            current_node = current_node.next
        return False


    def append(self, value) -> None:
        ''' Append the given value to the doubly linked list.

            Args:
                value: Value to be appended to the doubly linked list. Must support equality comparison.
        '''
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.size += 1
    

    def insert(self, index : int, value) -> None:
        ''' Inserts the given value into the given index.
        
            Args:
                value: Value to be added to the doubly linked list.
                index (int): Index at which value is to be added.
            
            Raises:
                IndexError: Index is out of bounds.
        '''

        new_node = Node(value)

        if index > self.size or index < 0:
            raise IndexError("Index out of bounds")
        
        # initialize list with new node
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # insert at the head
        elif index == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        
        # insert at the tail
        elif index == self.size:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        # traverse to target position and insert new node
        else:
            current_node = self.head
            current_index = 0
            while current_index < index:
                current_node = current_node.next
                current_index += 1
            prev_current_node = current_node.previous

            prev_current_node.next = new_node
            new_node.previous = prev_current_node

            new_node.next = current_node
            current_node.previous = new_node
    
        self.size += 1