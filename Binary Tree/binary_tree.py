from typing import Literal

class Node:
    ''' A node in a binary tree with a comparable value.

    Attributes:
        entry: Value of the node (must be comparable, e.g. int, string, float).
        left_child: Reference to the left child node.
        right_child: Reference to the right child node.
    '''
    def __init__ (self, entry):
        self.entry = entry
        self.left_child = None
        self.right_child = None

class BinaryTree:
    '''A binary set up by nodes with comparable values.

    Attributes:
        root: Reference to the root of the binary tree.
    '''

    def __init__(self):
        '''Initialize a new empty binary tree.'''
        self.root = None

    def insert(self, value):
        '''Insert a new node with the given value into the binary tree.
        
        Args:
            value: Value to insert. Must be comparable, e.g. int, str, float.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node : Node, value): 
        ''' Recursively insert a value into the subtree rooted at 'current_node'.
            Duplicate values are inserted into the right subtree.
            Internal helper method.

        Args:
            current_node (Node): The root of the subtree where the value is inserted.
            value: Value to insert. Must be comparable, e.g. int, str, float.
        '''
        if value < current_node.entry:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(current_node.right_child, value)

    def contains(self, value) -> bool:
        ''' Check if the given value is contained in the binary tree.

        Args:
            value: The value to search for in the binary tree.

        Returns:
            bool: True if value is contained in the binary tree, False otherwise.

        Raises:
            TypeError: If 'value' is not comparable to the values stored in the binary tree.
        '''
        if self.root is None:
            return False
        try:
            return self._contains(self.root, value)
        except TypeError:
            raise TypeError("Input must be comparable to values stored in tree")
    
    def _contains(self, current_node : Node, value) -> bool:
        ''' Recursively check if the given value is contained in the subtree rooted at 'current_node'.
            Internal helper method.

        Args:
            current_node (Node): The root of the subtree where the value is searched.
            value: The value to search for.
        
        Returns:
            bool: True if 'value' is found in 'current_node', otherwise False.
        
        '''
        if value == current_node.entry:
            return True
        elif value < current_node.entry and current_node.left_child is not None:
            return self._contains(current_node.left_child, value)
        elif value >= current_node.entry and current_node.right_child is not None:
            return self._contains(current_node.right_child, value)
        else:
            return False
    
    def delete(self, value):
        ''' Delete the given value from the binary tree.

        Args:
            value: Value to delete from the tree.
        '''
        self.root = self._delete(self.root, value)
    
    def _delete(self, current_node : Node, value):
        ''' Recursively delete a given value from the subtree rooted at 'current_node'.
            Internal helper method.
        
        Args:
            current_node (Node): Root of the subtree where 'value' is deleted.
            value: Value to delete from 'current_node'.
        '''

        if current_node is None:
            return None # base case: empty subtree
        if value < current_node.entry:
            # search for value in the left subtree
            current_node.left_child = self._delete(current_node.left_child, value)
        elif value > current_node.entry:
            # search for value in the right subtree
            current_node.right_child = self._delete(current_node.right_child, value)
        # node containing the value was found
        else:
            # case 1: node is a leaf (no children)
            if current_node.left_child is None and current_node.right_child is None:
                return None
            # case 2: node has only a left child
            elif current_node.right_child is None:
                return current_node.left_child
            # case 3: node has only a right child
            elif current_node.left_child is None:
                return current_node.right_child
            # case 4: node has two children
            else:
                # replace the node's value with the smallest value from the right subtree
                replacement_node = self._find_smallest_node(current_node.right_child)
                current_node.entry = replacement_node.entry
                # delete the duplicate value from the right subtree
                current_node.right_child = self._delete(current_node.right_child, current_node.entry)
        return current_node

    def _find_smallest_node(self, node : Node) -> Node:
        ''' Find the node with the smallest value from the subtree rooted at 'node'.
            Internal helper method.

        Args:
            node (Node): Root of the subtree from which the node with the smallest value is to be returned.

        Returns:
            Node: The node containing the smallest value from the subtree rooted at 'node'.
        '''
        smallest_node = node
        while smallest_node.left_child is not None:
            smallest_node = smallest_node.left_child
        return smallest_node
    

    def _traverse(self, order : Literal["pre", "in", "post"], function_applied):
        ''' Traverse the binary tree in the given order and apply a given function to each node.
            Internal helper method.

            Args:
                order: Traversal order ('pre', 'in', 'post').
                function_applied: Function applied to each node.
        '''
        if self.root is not None:
            if order == "pre":
                self._traverse_pre_order(self.root, function_applied)
            elif order == "in":
                self._traverse_in_order(self.root, function_applied)
            elif order == "post":
                self._traverse_post_order(self.root, function_applied)
            else:
                raise ValueError("order only allows the following arguments: 'pre', 'in' and 'post'")
    
    def _traverse_pre_order(self, current_node : Node, function_applied):
        ''' Traverse the binary tree in pre-order and apply a given function to each node.
            Internal helper method.

            Args:
                current_node (Node):  Root of the subtree that is to be traversed.
                function_applied: Function applied to each node.
        '''
        function_applied(current_node.entry)
        if current_node.left_child is not None:
            self._traverse_pre_order(current_node.left_child, function_applied)
        if current_node.right_child is not None:
            self._traverse_pre_order(current_node.right_child, function_applied)
    
    def _traverse_in_order(self, current_node : Node, function_applied):
        ''' Traverse the binary tree in in-order and apply a given function to each node.
            Internal helper method.

            Args:
                current_node (Node):  Root of the subtree that is to be traversed.
        '''
        if current_node.left_child is not None:
            self._traverse_in_order(current_node.left_child, function_applied) 
        function_applied(current_node.entry)
        if current_node.right_child is not None:
            self._traverse_in_order(current_node.right_child, function_applied)

    def _traverse_post_order(self, current_node : Node, function_applied):
        ''' Traverse the binary tree in post-order and apply a given function to each node.
            Internal helper method.

            Args:
                current_node (Node):  Root of the subtree that is to be traversed.
        '''
        if current_node.left_child is not None:
            self._traverse_post_order(current_node.left_child, function_applied)
        if current_node.right_child is not None:
            self._traverse_post_order(current_node.right_child, function_applied)
        function_applied(current_node.entry)

    def print_all_values(self, order : Literal["pre", "in", "post"]):
        ''' Print all values contained in the binary tree in the given order to the console.
            Args:
                order(Literal['pre', 'in', 'post']): Traversal order ('pre', 'in', 'post').
        
        '''
        self._traverse(order, print)

    def create_list_of_values(self, order : Literal["pre", "in", "post"]) -> list:
        ''' Return a list of all values contained in the binary tree in the given order.
        
            Args:
                order(Literal['pre', 'in', 'post']): Traversal order ('pre', 'in', 'post').
            
            Returns:
                list: All values in the tree in the specified traversal order.

            Raises:
                ValueError: If 'order' is invalid.
        '''
        if order not in ("pre", "in", "post"):
            raise ValueError("order only allows the following arguments: 'pre', 'in' and 'post'")
        
        value_list = []
        self._traverse(order, value_list.append)
        return value_list