class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def preorder_search(self, root, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        if root:
            print("nope")
            if self.root.value is find_val:
                print("nope1")
                return(True)
            self.preorder_search(root.left,find_val)
            self.preorder_search(root.right,find_val)
        else:
            # print("skdgkjghkgjv")
            return False

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes 
        if self.root is None:
            print("root",False)
            return False
        else:
            a =  self.preorder_search(self.root,find_val)
            print(a)
            return a
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        pass

    

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        pass
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.search(4))