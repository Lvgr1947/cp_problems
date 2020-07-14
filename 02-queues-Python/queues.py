"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        a = self.storage[0]
        self.storage[0] = new_element
        for i in range(len(1,self.storage)):
            if i==1:
                self.storage[i] = new_element
            self.storage[i] = self.storage[i+1]    
    def peek(self):
        pass 

    def dequeue(self):
        pass