"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(x):
    return lambda x: x if x<=1 else fib(x-1) + fib(x-2)