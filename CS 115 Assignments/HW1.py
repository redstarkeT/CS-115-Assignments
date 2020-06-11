"""Timothy Stephens, I pledge my honor that I have abided by the Stevens Honor System."""
from cs115 import map,range, reduce

#part A
def factorial(n):
    """Takes a positive integer n and returns n!"""
    if n==0:
        return 1
    if n==1:
        return 1
    else: return n*factorial(n-1);
    
#part B
def add(x,y):
    """Adds and returns two variables"""
    return x+y

def mean(L):
    """Returns the mean of a given list"""
    if L==[]:
        return 0
    else:
        count=len(L)
        quant=reduce(add,L)
        return quant/count

#idk why its giving error
#also how to include decimals 

#part C

#why does python say not defined
def divides(n):
    def div(k):
        return n % k == 0
    return div
#same python says not defined


    
def prime(n):
    """Takes a positive integer n as input and returns True or False"""
    return True not in map(divides(n),range(2,n))
    
        
    
    
