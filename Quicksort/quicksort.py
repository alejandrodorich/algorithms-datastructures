
def _calculate_pivot_index(lst: list, low_index: int, high_index: int) -> int:
    ''' Calculate the index of the pivot using the median-of-three method. 

        Args:
            lst (list): The list for which the pivot index is calculated.
            low_index (int): The starting index of the sublist.
            high_index (int): The ending index of the sublist.

        Returns:
            int: The index of the median-of-three pivot in the sublist.
    '''

    middle_index = (low_index + high_index) // 2

    first_elem = lst[low_index]
    middle_elem = lst[middle_index]
    last_elem = lst[high_index]

    if (middle_elem <= first_elem <= last_elem) or (last_elem <= first_elem <= middle_elem):
        return low_index
    elif (first_elem <= middle_elem <= last_elem) or (last_elem <= middle_elem <= first_elem):
        return middle_index
    else:
        return high_index

def _quicksort(lst: list, low_index: int, high_index: int) -> None:
    ''' Sort a subrange of the given list in-place using the quicksort algorithm.
        The pivot is selected using the median-of-three method and the function 
        recursively sorts the resulting sublists.

        Args:
            lst (list): The list to be sorted (in-place).
            low_index (int): The starting index of the sublist.
            high_index (int): The ending index of the sublist.

        Note:
            - Internal helper method.
            - The original list is modified in-place; no return value.
    '''

    if low_index >= high_index:
        return

    left_pointer = low_index
    right_pointer = high_index
    
    pivot_index = _calculate_pivot_index(lst, low_index, high_index)
    pivot = lst[pivot_index]

    # move pivot to the end of the list
    lst[pivot_index], lst[high_index] = lst[high_index], lst[pivot_index]
    right_pointer = high_index - 1

    # Partition the list around the pivot
    while left_pointer < right_pointer:

        while lst[left_pointer] <= pivot and left_pointer < right_pointer:
            left_pointer += 1

        while lst[right_pointer] >= pivot and left_pointer < right_pointer:
            right_pointer -= 1

        if left_pointer < right_pointer:
            lst[left_pointer], lst[right_pointer] = lst[right_pointer], lst[left_pointer]

    # move pivot to its final sorted position
    lst[left_pointer], lst[high_index] = lst[high_index], lst[left_pointer]
  
    _quicksort(lst, low_index, left_pointer - 1)
    _quicksort(lst, left_pointer + 1, high_index)

def quicksort(lst: list) -> list:
    ''' Return a sorted copy of the given list using the Quicksort algorithm.
        The pivot is selected using the median-of-three method and the function 
        recursively sorts the resulting sublists.
    
        Args:
            lst (list): The list to be sorted.

        Returns:
            list: The sorted list.
    '''
    if not isinstance(lst, list):
        raise TypeError(f"Expected list, got: {type(lst).__name__}")
    
    result = lst.copy()
    if len(lst) > 1:    
        _quicksort(result, 0, len(lst)-1)

    return result
