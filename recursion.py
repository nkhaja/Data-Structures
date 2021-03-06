#!python

import unittest


def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)

    return factorial_recursive(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    pass
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests below

    if n < 0 || type(n) is not int:
        raise ValueError

    product = 1
    for i in range(n, - 1):
        product = product * i + 1
    return product




def factorial_recursive(n):
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)
