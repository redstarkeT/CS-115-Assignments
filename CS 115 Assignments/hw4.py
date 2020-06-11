'''
Created on 2/26/20
Author: Timothy Stephens
Pledge: I pledge that I have abided by the Stevens Honor System.

CS115 - HW4
'''
from cs115 import *

def pascal_helper1(L):
    '''Reduces the list by adding adjacent elements from left to right'''
    if L==[] or len(L)==1:
        return []
    else:
        return [L[0]+L[1]]+pascal_helper1(L[1:])

    
def pascal_row(n):
    '''Outputs the row of pascal that corresponds with n'''
    if n==0:
        return [1]
    if n==1:
        return [1,1]
    else:
        return [1] + pascal_helper1(pascal_row(n-1)) + [1]


def pascal_triangle(n): 
    '''Outputs the recursive list of rows of pascal up to and including
    the input n'''
    if n==0:
        return [[1]]
    return pascal_triangle(n-1) + [pascal_row(n)]


def test_pascal_row():
    '''Tests pascal row'''
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(4) == [1,4,6,4,1]
    assert pascal_row(3) == [1,3,3,1]
    assert pascal_row(2) == [1,2,1]

def test_pascal_triangle():
    '''Test pascal triangle'''
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1]]
