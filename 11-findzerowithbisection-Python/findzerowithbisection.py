# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.
import math
def findzerowithbisection(x, i): 
# def Square(n, i, j):  
    j = i; 
  # While the square root is not found 
    found = False; 
    while (found == False): 
  
        # If n is a perfect square 
        if (j * j == x): 
            return(j)
            found = True
          
        elif (j * j > x): 
  
            # Square root will lie in the 
            # interval i-1 and i 
            res = findzerowithbisection(x, j - i); 
            return(res)  
            found = True
        j += 1; 
print(findzerowithbisection(25,0.01))