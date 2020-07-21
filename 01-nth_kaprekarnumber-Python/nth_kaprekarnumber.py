# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def knumber(x):
    y = x**2
    y1 = y // (10**(((len(str(y)))//2)+1))
    # print( "before",y1)
    y2 = y % (10**(len(str(y))//2))
    # print("after",y1)
    y2 = y1+y2
    if x == y2:
        print("knumber",x)
        return True
    elif y1>0:
        y3 = str(y1)
        print(y3)
        y3 = y3.strip("0")
        y2 += int(y3) - y1
        if y2 == x:
            print("knumber",x)
            return True
        else:
            return False
    return False
def fun_nth_kaprekarnumber(n):
    i , j =  0 , 2
    if n == 0:
        return 1
    while(i<n):
        if knumber(j):
            i += 1
        j += 1
    return j-1
# print(fun_nth_kaprekarnumber(20), "final")
print(knumber(10))