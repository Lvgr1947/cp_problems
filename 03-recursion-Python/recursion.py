"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(x):
    if x<=1:
        return x
    else:
        return get_fib(x-1)+get_fib(x-2)

get_fib(9)