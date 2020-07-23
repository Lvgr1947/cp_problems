# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
def isprime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0):return False    
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):return False
        i = i + 6
    return True
def isugly(n):
    i = 2
    l = [2,3,5]
    check =0
    while(i < n//2 +1):
        if isprime(i) and n%i == 0:
            check = 1
            if i not in l:
                return False
        i += 1
    if check == 1:return True
    return False
def fun_nth_uglynumber(n):
    i , j = -1 , 1
    while(i<n):
        if isugly(j):
            i += 1
        j += 1
    return j-1
print(fun_nth_uglynumber(0))
print(fun_nth_uglynumber(1))
print(fun_nth_uglynumber(2))
print(fun_nth_uglynumber(3))
print(fun_nth_uglynumber(10))
