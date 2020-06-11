'''
Created on 2/17/20
@author:   Timothy Stephens
Pledge:    I pledge that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
from cs115 import *
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0                 
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount,coins):
    """Evaluates a desired amount of money and a set of coins to determine both
    the smallest number of coins needed and their specific list."""
    if amount==0:
        return [0,[]]
    if coins==[]:
        return [float('inf'),[]]
    if amount < coins[0]:
        return giveChange(amount, coins[1:])
    else:
        lose= giveChange(amount,coins[1:])
        use= giveChange(amount-coins[0],coins)
        if use[0] < lose[0]:
            second = use[1] + [coins[0]]
            lst= [use[0]+1, second]
            return lst
        else:
            return lose
        
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    """ takes as input a single letter string called letter
    and a list where each element in that list is itself a list of the form"""
    if scorelist == []:
        return []
    if scorelist[0][0]==letter:
        return scorelist[0][1]
    else:
        return letterScore(letter,scorelist[1:])
        
def wordScore(S, scorelist):
    """should take as input a string S and a scorelist in the format described above,
    which will have only lowercase letters, and should return as output the scrabble score
    of that string."""
    if S == "":
        return 0
    else:
        return letterScore(S[0],scorelist)+wordScore(S[1:],scorelist)
    
def wordsWithScore(dct, scores):
    '''List of words in dct, with their resepctivce Scrabble score
    concatenated within a list. For example, wordsWithScore(Dictionary,
    scrabbleScores) should return [['a', 1], ['am', 4], ['at', 2] ...etc... ]'''
    if dct==[]:   #this is for when the word list is empty
        return []
    return [[dct[0],wordScore(dct[0],scores)]] + wordsWithScore(dct[1:],scores)
                  # your code goes here



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n==0:
        return []
    if L==[]:
        return []
    else:
        n=n-1
        return [L[0]] + take(n,L[1:])




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if L==[]:
        return ""
    if n==0:
        return L[0:]
    else:
        n=n-1
        return drop(n,L[1:])
    return None  # your code goes here


