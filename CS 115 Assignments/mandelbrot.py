# mandelbrot.py
# Lab 9
#
# Name:Timothy Stephens
# Honor: I pledge my honor that I have abided with the Stevens Honor System.
# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    '''mult uses only a loop and addition
    to multiply c by the integer n'''
    result = 0
    for x in range(n):
        result += c #adds n c times 
    return result

print(mult(3,10))
print(mult(1.5,10))
print(mult(1.99,10))

def update(c,n):
    '''update starts with z=0 and runs z = z**2 + c
    for a total of n times. Its returns the final z.'''
    z = 0 
    for x in range(n):
        z = z**2 + c
    return z   

print(update(1,3)) #should be 5
print(update(-1,10)) #should be 0

def inMSet(c, n):
    """takes as input a complex number c and an integer n; returns True
    if complex number c is in Mandelbrot set and False otherwise.""" 
    z = 0 
    for x in range(n):
        z = z**2 + c 
        if abs(z) > 2:
            return False
    if abs(z) <2:
        return True

c = 3 + 4j #test in run
