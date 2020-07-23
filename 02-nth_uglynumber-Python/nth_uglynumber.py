# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def isugly(n):
    i = 2
    l = [2,3,5]
    while(i < n//2 +1):
        if isprime(i) and n%i == 0:
            if i not in l:
                return False
        i += 1
    return True
def fun_nth_uglynumber(n):
    i , j = -1 , 1
    while(i<n):
        if isugly(j):
            i += 1
        
