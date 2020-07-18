class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):

    def __init__(self, root):
        self.root = Node(root)


    def search_bst(self,root,key): 
      
    # Base Cases: root is null or key is present at root 
        if root is None:
            return False
        elif root.value == key: 
            return True
    
        # Key is greater than root's key 
        if root.value < key: 
            return self.search_bst(root.right,key) 
        
        # Key is smaller than root's key 
        return self.search_bst(root.left,key)

    def search(self,key):
        return self.search_bst(self.root,key)

    def printSelf(self):
        pass
        # if self.root is None:
        #     print("None")
        # else:
        #     print(self.root.left)
        #     print(self.root.right)
    def insert(self,key):
        node = Node(key)
        y = 0
        x = self.root
        while x!= None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
    # def insert(self, key):
	# 	node = Node(key)
    #     y = None
    #     x = self.root
    #     while x != None:
    #         y = x
    #         if node.value < x.data:
	# 			x = x.left
	# 		else:
	# 			x = x.right

		# y is parent of x
		# node.parent = y
		# if y == None:
		# 	root = node
		# elif node.data < y.data:
		# 	y.left = node
		# else:
		# 	y.right = node
        
       
tree = BST(4)
(tree.insert(2))
print(tree.insert(1))
(tree.insert(3))
tree.insert(5)
print(tree.search(5))