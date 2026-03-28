from quicksort import quicksort

def try_invalid_value(function):
    ''' Return True if the given function raises a TypeError, otherwise return False.
    
        Args:
            function (callable): Function to be executed and tested for TypeErrors.'''
    try:
        function()
        return False
    except TypeError:
        return True

def test_core_sorting():
    ''' Test core sorting functionality with standard cases, including pivot positions. '''

    test_lists = [
    [42, 8, 15, 47, 11, 17, 23, 4, 52, 84], # initial pivot at the beginning
    [84, 8, 15, 47, 11, 17, 23, 4, 52, 42], # initial pivot at the end
    [84, 8, 15, 47, 42, 17, 23, 4, 52, 11], # initial pivot at the center
    [4, 8, 11, 15, 17, 23, 42, 47, 52, 84], # sorted list
    ]

    for test_list in test_lists:
        assert  quicksort(test_list) == sorted(test_list)


def test_edge_cases_sorting():
    ''' Test edge cases for sorting, including empty lists, duplicates, and negatives. '''

    test_lists = [
    [4, 8, 11, 15, 17, 23, 17, 47, 52, 84], # duplicate values
    [4, 8, 11, -15, 0, 23, 17, -47, 52],    # negative values
    [4, 4, 4, 4, 4, 4],                     # only equal values
    [84, 42],                               # unsorted list, two elements
    [42, 84],                               # sorted list, two elements         
    [42],                                   # list with one element
    []                                      # empty list
    ]

    for test_list in test_lists:
            assert  quicksort(test_list) == sorted(test_list)


def test_invalid_values():
    ''' Test quicksort with invalid values. '''
      
    assert try_invalid_value(lambda: quicksort("This is a string"))
    assert try_invalid_value(lambda: quicksort(None))
    assert try_invalid_value(lambda: quicksort(42))
        