'''
Created on March 11, 2020
@author:   Timothy Stephens
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.



# COMPRESS (Naumann used recursion to implement these)

def prefix(b, S):
    '''Assuming b is integer 0 or 1, how many of character b does S begin with.'''
    if len(S)== 0:
        return 0
    elif S[0] == str(b):
        return 1 + prefix(b,S[1:])
    else:
        return 0

# EX: assert prefix(0, '00011') == 3 and prefix(0, '111') == 0 and prefix(0, '10010') == 0


def compress(S):
    '''Takes a binary string S of legnth 64 as input and returns another binary string as
    a run-length encoding of the input string.'''
    if S=='':
        return ''
    def comp(S,b):
        '''Assume b is integer 0 or 1 and S a string. Compress starting with b.'''
        if S=='':
            return ''
        if b==0:
            n=prefix(b,S)
            if n > 31:
                return numToBinPadded(31) + comp(S[31:],1)
            else:
                return numToBinPadded(n) + comp(S[n:],1)
        if b==1:
            n=prefix(b,S)
            if n > 31:
                return numToBinPadded(31) + comp(S[31:],1)
            else:
                return numToBinPadded(n) + comp(S[n:],0)
    return comp(S,0)

#0 times 64
#1111100000111110000000010
#1111100000111110000000010
#1111100000111110000000010

#UNCOMPRESS (hint: use map)

def uncompress(C):
    '''Inverts or undeoes the compressing in your compress function.'''
    if C=='':
        return ''
    def uncomp(C,b):
        '''Assume b is integer 0 or 1 and S a string. Compress starting with b.'''
        if C=='':
            return ''
        if b==0:
            return '0'*binaryToNum(C[0:5]) + uncomp(C[5:],1)
        if b==1:
            return '1'*binaryToNum(C[0:5]) + uncomp(C[5:],0)
    return uncomp(C,0)


def compression(S):
    "returns the ratio of the compressed size string to the original size string of image S"
    return len(compress(S)) / len(S)

# helpers

def bitToChar(b):
    assert b==0 or b==1
    return chr(b + ord('0'))

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

def numToBinPadded(n):
    '''Assume 0 <= n <= MAX_RUN_LENGTH. Return binary representation of n
        padded with leading 0s to have length COMPRESSED_BLOCK_SIZE.
        For example, numToBinPadded(3) is *00011*.'''
    s = numToBinary(n)
    pad = '0'*(COMPRESSED_BLOCK_SIZE - len(s))
    return pad + s

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1
