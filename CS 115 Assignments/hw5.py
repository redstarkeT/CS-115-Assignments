'''
Created on March 2, 2020
@author:   Timothy Stephens
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code System.

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

turtle.left(89)
    
def sv_tree(trunk_length, levels):
    '''Recursively draws a stick figure of a tree using trunk_length
    and levels as parameters'''
    turtle.shape("turtle")

    if levels==0:
        return 
    else:   
        turtle.forward(trunk_length)
        turtle.left(45)
        sv_tree(trunk_length/2,levels-1)
        turtle.right(90)
        sv_tree(trunk_length/2,levels-1)
        turtle.left(45)
        turtle.backward(trunk_length)

    

memo={}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if (n) in memo:
        return memo[(n)]
    if n==0:
        result = 2
    elif n==1:
        result = 1
    else:
        result = fast_lucas(n-1) + fast_lucas(n-2)
    memo[(n)]=result
    return result

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo2):
        if (amount,coins) in memo2:
            return memo2[(amount,coins)]
        elif amount==0:
            result=0
        elif coins==():
            result=float('inf')
        elif amount < coins[0]:
            result=fast_change_helper(amount, coins[1:],memo2)
        else:
            lose=fast_change_helper(amount,coins[1:],memo2)
            use=1+fast_change_helper(amount-coins[0],coins,memo2)
            result=min(use,lose)
        memo2[(amount,coins)]=result
        return result
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
