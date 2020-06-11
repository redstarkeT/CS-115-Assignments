'''
Created on March 5, 2020
@author:   Timothy Stephens
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2)+ str(1)
    else:
        return numToBinary(n//2) + str(0)
    
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    if len(s) == 1:
        return (binaryToNum(s[:-1]) + int(s))
    return (binaryToNum(s[:-1])* 2) + int(s[-1])


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    first=binaryToNum(s)+1
    second=numToBinary(first)
    if len(second)>=8:
        return second[-8:]
    else:
        omega=(8-len(second))*'0'+second
        return omega

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n==0:
        return
    else:
        return count((increment(s)),n-1)

    

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    else:
        return numToTernary(n//3) + str((n%3))
    

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    if len(s) == 1:
        return (ternaryToNum(s[:-1]) + int(s))
    return (ternaryToNum(s[:-1])* 3) + int(s[-1])


