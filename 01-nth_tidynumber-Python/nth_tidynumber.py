# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def istidy(n):
    n = list(map(int,str(n)))
    m = sorted(n)
    if m == n:
        return True
    return False
def fun_nth_tidynumber(n):
    i , j = -1,