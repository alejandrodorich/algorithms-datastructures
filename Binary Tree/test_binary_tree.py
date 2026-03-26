
from binary_tree import BinaryTree

empty_tree = BinaryTree()
test_values = [25, 17, 40, 19, 30, 8, 27, 45]
expected_outcome_pre_order = [25, 17, 8, 19, 40, 30 , 27 , 45] # Pre-order sequence of 'test_values'
expected_outcome_in_order = sorted(test_values) # In-order sequence of 'test_values'
expected_outcome_post_order = [8, 19, 17, 27, 30, 45, 40, 25] # Post-order sequence of 'test_values'


def try_invalid_value(function):
    ''' Return True if the given function raises a Value- or TypeError, otherwise return False.
    
        Args:
            function (callable): Function to be executed and tested for Value- or TypeErrors.'''
    try:
        function()
        return False
    except (ValueError, TypeError):
        return True

def test_insert_and_contains():
    ''' Test insert and contain methods.'''

    # test insert method 
    bin_tree = BinaryTree()

    for value in test_values:
        bin_tree.insert(value)

    # test contains method
    for value in test_values:
        assert bin_tree.contains(value)

    assert not empty_tree.contains(25)

def test_invalid_values():
    ''' Test insert and contains methods with invalid values.'''
    bin_tree = BinaryTree()
    bin_tree.insert(2)

    assert try_invalid_value(lambda: bin_tree.create_list_of_values("text"))
    assert try_invalid_value(lambda: bin_tree.contains(None))

def test_duplicates():
    ''' Test insert and delete methods with duplicate values'''

    new_tree = BinaryTree()
    new_tree.insert(25)
    new_tree.insert(25)

    assert new_tree.create_list_of_values("pre") == [25, 25]

    new_tree.delete(25)
    assert new_tree.create_list_of_values("pre") == [25]

def test_traversal():
    ''' Test traveral and create list methods in pre-, in- and post-order.'''

    bin_tree =  BinaryTree()

    # insert values into 'bin_tree'

    for value in test_values:
        bin_tree.insert(value)
    
    #test traverse and create list methods in pre-order sequence
    actual_outcome_pre_order = bin_tree.create_list_of_values("pre")
    assert actual_outcome_pre_order == expected_outcome_pre_order
    assert empty_tree.create_list_of_values("pre") == []

    # test traverse and create list methods in in-order sequence
    actual_outcome_in_order = bin_tree.create_list_of_values("in")
    assert expected_outcome_in_order == actual_outcome_in_order
    assert empty_tree.create_list_of_values("in") == []

    # test traverse and create list methods in post-order sequence
    actual_outcome_post_order = bin_tree.create_list_of_values("post")
    assert expected_outcome_post_order == actual_outcome_post_order
    assert empty_tree.create_list_of_values("post") == []

def test_delete():
    ''' Test delete method.'''

    # insert values into 'bin_tree'
    bin_tree = BinaryTree()
    for value in test_values:
        bin_tree.insert(value)

    delete_values = [27, 40, 25] # leaf, inner and root values of 'bin_tree'

    # delete all elements in 'delete_values' out of 'bin_tree' and check if ouctomes are correct
    for del_val in delete_values:
        bin_tree.delete(del_val)
        actual_current_outcome = bin_tree.create_list_of_values("in")
        expected_outcome_in_order.remove(del_val)
        assert actual_current_outcome == expected_outcome_in_order



