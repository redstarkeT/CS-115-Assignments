"""Timothy Stephens, I pledge my honor that I have abided by the Stevens Honor System."""
from math import factorial
from cs115 import reduce
import math
def inverse(n):
    """This function returns the inverse of the number plugged in."""
    return 1/n
def add(x,y): return x+y
def e(n):
    """This function returns the summation of 1+1/n!"""
    Step1=list(range(1,n+1))
    Step2=list(map(factorial,Step1))
    Step3=list(map(inverse,Step2))
    Step4=reduce(add,Step3)
    Step5=1+Step4
    return Step5
def error(n):
    """This function returns the absolute value of the difference between math.e and e(n)."""
    diff=math.e - e(n)
    return abs(diff)


#e(n):
#Algorithm copied down from written stuff (sort of like proofs from discrete working backwards)
#Step 1: Make a range from 1 to n+1
#Step 2: Apply summation on all of list using map
#Step 3: Apply an inverse function on all of list using map
#Step 4: Apply add to all the numbers using reduce
#Step 5: Add answer to +1 for final answer
#goal is to return 1+1/1!+1/2!+1/3!+...+1/n!

#>>>import math
#>>> math.e
#2.718281828459045
#>>> math.factorial(2)
#2
#>>> abs(-1)
#1
