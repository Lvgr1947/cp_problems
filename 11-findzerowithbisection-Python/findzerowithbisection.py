# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.
import math
def findzerowithbisection(x, i): 
# def Square(n, i, j): 
	
    mid = (i + j) / 2; 
    mul = mid * mid; 
  
    # If mid itself is the square root, 
    # return mid 
    if ((mul == n) or (abs(mul - n) <epsilon)): 
        return mid; 
  
    # If mul is less than n, recur second half 
    elif (mul < n): 
        return Square(n, mid, j); 
  
    # Else recur first half 
    else: 
        return Square(n, i, mid); 
  
# Function to find the square root of n 
def findSqrt(n): 
    i = 1; 
  
    # While the square root is not found 
    found = False; 
    while (found == False): 
  
        # If n is a perfect square 
        if (i * i == n): 
            print(i); 
            found = True; 
          
        elif (i * i > n): 
  
            # Square root will lie in the 
            # interval i-1 and i 
            res = findzerowithbisection(n, i - 1); 
            print (res)  
            found = True
        i += 1; 
  