"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(x):
    a =[lambda x: x if x<=1 else get_fib(x-1) + get_fib(x-2)]
    
print(get_fib(9))