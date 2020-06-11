'''
Created on 2/11/2020
@author:   Timothy Stephens
Pledge:    I pledge that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
from cs115 import *
# Be sure to submit hw2.py.  Remove the '_template' from the file name.
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.



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
    
def removeOne(e,L):
    """Takes in an element e and a list L to remove all the e's from that given list"""
    if L==[]:
        return []
    if L[0]==e:
        return L[1:]
    else:
        return [L[0]] + removeOne(e, L[1:])
    
A="apple"
Rack=["p","l","a","p","m","k","e"]
def isWIR(A,Rack):
    if A=="":
        return True
    if Rack==[]:
        return False
    if A[0]in Rack:
        Rack=removeOne(A[0],Rack)
        return isWIR(A[1:],Rack)
    else:
        return False

def scoreList(Rack):
    listOfWords = filter(lambda word : isWIR(word,Rack), Dictionary)
    """Map wordScore to each word? but in this case you edit the function and make
    a new helper function that concatenates the wordScore next to the word in the list"""
    def wordAndScoreList(word):
        return [word,wordScore(word,scrabbleScores)]
    return map(wordAndScoreList, listOfWords)

def HighestFinder(x,y):
    """compares x and y to find the highest score"""
    highest = 0
    if x[1] < y[1]:
        return y
    else:
        return x

def bestWord(Rack):
     """takes as input a Rack as above and returns a list with
     two elements: the highest possible scoring word from that
     Rack followed by its score."""
     if scoreList(Rack) == []:
         return ["",0]
     else:
         return reduce(HighestFinder, scoreList(Rack))

    

"""write that helper function that takes a word and returns a list of that
word and its score, and then you map that help function to your words"""
