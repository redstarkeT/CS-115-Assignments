'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Lab 5
'''
import time
from cs115 import map
from cs115 import *

words = []
HITS = 10

memo= {} #dictionary for use in fastED; keys are tuples (str1, str2)
def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    
    def fast_ED_helper(first,second,memo, indent):
        #if key exists, return value already associated with key.
        print("  "*indent+"fast_ED_helper("+first+", "+ second+")")
        if (first,second) in memo:
            return memo[(first,second)]

        #Do work.
        if first == '':
            memo[(first,second)] = len(second)
            return len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            result = fast_ED_helper(first[1:], second[1:], memo, indent+1)
        else:
            substitution = 1 + fast_ED_helper(first[1:], second[1:], memo, indent+1)
            deletion = 1 + fast_ED_helper(first[1:], second, memo, indent+1)
            insertion = 1 + fast_ED_helper(first, second[1:], memo, indent+1)
            result = min(substitution,deletion, insertion, indent+1)
        # Store and return result.
        memo[(first, second)] = result
        return result
    return fast_ED_helper(first, second, {}, 0)

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    
    return map(lambda word:(fastED(user_input,word),word), words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()


