class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes 
        if self.root is None:
            return True
        elif preorder_search(self.root):
            return True
        else:
            return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        if start:
            if start.value is find_val:
                return(True)
            preorder_search(root.left,find_val)
            preorder_search(root.right,find_val)
        else:
            return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        pass
