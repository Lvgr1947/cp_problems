class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):

    def __init__(self, root):
        self.root = Node(root)


    # def insert_bst(self, root, val):
    #     if root is None: 
    #             root.value = val 
    #     else: 
    #         if self.root.value < val: 
    #             if self.root.right is None: 
    #                 self.root.right = val 
    #             else: 
    #                 self.insert_bst(self.root.right, val) 
    #         else: 
    #             if self.root.left is None: 
    #                 self.root.left = val 
    #             else: 
    #                 self.insert_bst(self.root.left, val)

    def search(self, e):
        d = Node(e)
        type(d.value)
        if self.root is not None:
            if self.root == d:
                return True
            elif 3 < int(self.root.value):
                if self.root.left:
                    self.root = self.root.left
                    return self.search(d)
            elif d.value > self.root.value:
                if self.root.right:
                    self.root = self.root.right
                    return self.search(d)
        else:
            return False

    def printSelf(self):
        pass
        # if self.root is None:
        #     print("None")
        # else:
        #     print(self.root.left)
        #     print(self.root.right)
        
    def insert(self, d):
        if self.root is None:
            return False
        elif self.root.value == d:
            return True
        elif d < self.root.value:
            if self.root.left:
                self.root = self.root.left
                return self.insert(d)
            else:
                self.root.left = Node(d)
                return True
        else:
            if self.root.right:
                self.root = self.root.right
                return self.insert(d)
            else:
                self.root.right = Node(d)
                return True
        
       
tree = BST(4)
(tree.insert(2))
print(tree.insert(1))
(tree.insert(3))
tree.insert(5)
print(tree.search(5))