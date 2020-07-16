"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        while(self.head.next):
            self.head = self.head.next
        self.head.next = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        count = 1
        while(self.head is not None):
            if(count == position):
                return self.head.value
            self.head = self.head.next
            count += 1
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count = 1
        while(self.head is not None):
            if(count == position-1):
                break
            count += 1
        newNode = LinkedList(new_element)
        self.head.next = newNode
        newNode.next = self.head.next.next
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        if self.head != None:
            while(self.head is not None):
                if(self.head.value == value):
                    self.head = self.head.next
                    break
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
print(ll.get_position(e1))