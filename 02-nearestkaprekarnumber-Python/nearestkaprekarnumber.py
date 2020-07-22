# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.


import math
def knumber(x):
    y = x**2
    b = len(str(y))
    if b%2 != 0:
        b += 1
    y1 = y // (10**(b//2))
    y2 = y % (10**(b//2))
    y2 = y1+y2
    if x == y2: return True
    elif y1>0:
        y3 = str(y1)
        y3 = y3.strip("0")
        y2 += int(y3) - y1
        if y2 == x:return True
        return False
    return False
def fun_nearestkaprekarnumber(n):
    i = 0
    j = 2
    while(True):
        if knumber(j):
            if 
            if abs(j-n) < abs(i-n):
                return j
            elif abs(j-n) == abs(i-n):
                return min(i,j)
            i = j
        j += 1
print(fun_nearestkaprekarnumber(47))
