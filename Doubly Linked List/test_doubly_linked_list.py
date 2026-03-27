from doubly_linked_list import DoublyLinkedList

empty_linked_list = DoublyLinkedList()
test_values = [42, 8, 15, 47, 0, 11, 17, -9, 4, 52, -7]  # test input values for doubly linked list

test_linked_list = DoublyLinkedList()
for value in test_values:
    test_linked_list.append(value)


def check_equality(linked_list : DoublyLinkedList, lst : list) -> bool:

    ''' Compare if 'linked_list' and regular list contain the same values.
    
        Args:
            linked_list(DoublyLinkedList): Doubly linked list to be compared.
            lst(list): Classic Python list to be compared.

        Return:
            bool: True if both lists contain the same values, otherwise False.
    '''

    if len(linked_list) != len(lst): 
        return False
   
    for i, elem in enumerate(linked_list):
        if elem != lst[i]:
            return False
        
    return True


# checks if function raises an index or value error
def try_in_empty_list(function):
    ''' Return True if the given function raises a an Index- or ValueError, otherwise return False.
    
        Args:
            function (callable): Function to be executed and tested for Index- or ValueError.'''

    try:
        function()
        return False
    except (IndexError, ValueError):
        return True
    

def test_append_and_get():
    ''' Test append and get functionality. '''

    my_linked_list = DoublyLinkedList()

    # populate doubly linked list using append
    for value in test_values:
        my_linked_list.append(value)

    # verify that list size and element order are correct using get
    assert len(my_linked_list) == len(test_values)
    for i in range(len(my_linked_list)):
        assert my_linked_list.get(i) == test_values[i]

    # accessing empty doubly linked list should raise an error
    assert try_in_empty_list(lambda: empty_linked_list.get(0))

    # getting an out of bounds index should raise an error
    assert try_in_empty_list(lambda: test_linked_list.get(9999))

    # getting a negative index should raise an error
    assert try_in_empty_list(lambda: test_linked_list.get(-1))


def test_delete():
    ''' Test delete functionality. '''

    # setup doubly linked list and comparable list
    my_linked_list = DoublyLinkedList()
    for value in test_values:
        my_linked_list.append(value)
    test_values_copy = test_values.copy()

    # get edge values for the test
    middle_value = test_values_copy[len(test_values_copy) // 2]
    first_value = test_values_copy[0]
    last_value = test_values_copy[-1]

    delete_values = [middle_value, first_value, last_value]

    # delete values from middle, head, and tail positions
    for del_value in delete_values:
        my_linked_list.delete(del_value)
        test_values_copy.remove(del_value)
        assert check_equality(my_linked_list, test_values_copy)
    
    # deletion on an empty doubly linked list should raise an error
    assert try_in_empty_list(lambda: empty_linked_list.delete(0))

    # deletion of a non existing value should raise an error
    assert try_in_empty_list(lambda: test_linked_list.delete(9999))


def test_pop():
    ''' Test pop functionality. '''

    # setup doubly linked list and comparable list
    my_linked_list = DoublyLinkedList()
    for value in test_values:
        my_linked_list.append(value)
    test_values_copy = test_values.copy()

    # pop all values out of doubly linked list and verify list after every step
    while len(my_linked_list) > 0:
        assert my_linked_list.pop() == test_values_copy.pop()
        assert check_equality(my_linked_list, test_values_copy)

    # pop on an empty doubly linked list should raise an error
    assert try_in_empty_list(lambda: empty_linked_list.pop())


def test_iterability():
    ''' Test iterability. '''
    i = 0
    for value in test_linked_list:
        assert value == test_values[i]
        i += 1


def test_index_of():
    ''' Test 'index_of' functionality. '''

    # verify that the index matches positions in 'test_values'
    for i, value in enumerate(test_values):
        assert test_linked_list.index_of(value) == i

    # calling 'index_of' on an empty doubly linked list should raise an error
    assert try_in_empty_list(lambda: empty_linked_list.index_of(5))

    # getting the index of a non existing value should raise an error
    assert try_in_empty_list(lambda: test_linked_list.index_of(9999))


def test_insert():
    ''' Test insert functionality. '''

    # edge indices: middle, first, last
    index_list = [len(test_linked_list)//2, 0, len(test_linked_list)-1]
    insert_values = [15, 23, -9]

    # insert values at edge indices and verify
    for index, value in zip(index_list, insert_values):
        test_linked_list.insert(index, value)
        test_values.insert(index, value)
        assert check_equality(test_linked_list, test_values)

    # verify insertion into empty doubly linked list
    empty_linked_list.insert(0, 5)
    assert empty_linked_list.get(0) == 5
    empty_linked_list.pop()

    # insert should raise an error for an index larger than the list
    assert try_in_empty_list(lambda: test_linked_list.insert(9999, 9999))

    # insert should raise an error for a negative index
    assert try_in_empty_list(lambda: test_linked_list.insert(-1, 9999))

def test_contains():
    ''' Test contains functionality. '''

    # verify that every element in the doubly linked list is found
    for value in test_values:
        assert test_linked_list.contains(value)

    # check if an empty doubly linked list contains an element should return False
    assert not empty_linked_list.contains(5) 

     # check if an doubly linked list contains an element not on the list should return False
    assert not test_linked_list.contains(9999) 

    
