
'''

Name: Timothy Stephens
Date: March 28, 2020
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

'''

from cs115 import *

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder =
{ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def numToBaseB(N,B):
    '''takes as input a non-negative (0 or larger) integer N
    and a base B (between 2 and 10 inclusive) and returns a
    string representing the number N in base B. '''
    if N == 0:
        return str(N)
    def numToBaseBH(N,B):
    '''Helper function for numToBaseB'''
        if N == 0:
            return str(N)
        else:
            return numToBaseBH(int(N)//B,B) + str(int(N)%B)
    return numToBaseBH(N,B)

def baseBToNum(S,B):
    ''' takes as input a string S and a base B where S represents
    a number in base B where B is between 2 and 10 inclusive.'''
    if S == '':
        return 0
    else:
        return (int(S[0])*(B**(len(S)-1))) + baseBToNum(S[1:],B)

def baseToBase(B1,B2,SinB1):
    ''' takes three inputs: a base B1, a base B2 (both of which are
    between 2 and 10, inclusive) and SinB1, which is a string
    representing a number in base B1'''
    return numToBaseB(str(baseBToNum(SinB1,B1)),B2)

def add(S,T):
    '''takes two binary strings S and T as input and returns their sum,
    also in binary'''
    n1 = baseBToNum(S,2)
    n2 = baseBToNum(T,2)
    num = n1 + n2
    return numToBaseB(num,2)

def addB(S,T):
    '''returns a new string representing the sum of the two input strings'''
    def addBH(S,T,X,Y):
        '''Helper function for addB'''
        if len(S) < len(T):
            S = ('0'*(len(T)-len(S))) + S
        else:
            T = ('0'*(len(S)-len(T))) + T
        if T == '' or S == '':
            if Y == '1':
                return Y + X
            else:
                return X
        if ((S[len(S)-1]),(T[len(T)-1]),Y) in FullAdder:
            num = X
            X, Y = FullAdder[(Y, S[len(S)-1], T[len(T)-1])]
            X+= num
            return addBH(S[:(len(S)-1)], T[:(len(T)-1)], X, Y)
    return addBH(S,T,'','0')

