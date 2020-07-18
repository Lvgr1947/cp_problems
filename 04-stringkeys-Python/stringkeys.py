"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        i = 0
        self.table[i] = string
        # return self.table
        print(self.table)
        # i +=1
        # pass
    def calculate_hash_value(self, string):
        """Helper function to calulate 
        hash value from a string."""
        # Your code goes here
        hash_val = ((ord(string[0])) * 100) + ord(string[1])
        return hash_val    
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        x = self.table
        for i in x:
            if i == string:
                # calculate_hash_value(self,i)
                y = ((ord(string[0])) * 100) + ord(string[1])
                return y
        return -1