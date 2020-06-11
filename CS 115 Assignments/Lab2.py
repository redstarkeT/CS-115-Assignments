"""Timothy Stephens, I pledge my honor that I have abided by the Stevens Honor System."""
#part A
def dot(L,K):
    """Should Output the dot product of the lists K and K"""
    if L==[] or K==[]:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

#part B
def explode(S):
    """Should take a string S as input and should return a list of characters."""
    if S =="":
        return []
    else:
        return [S[0]] + explode(S[1:])
#part C
def ind(e,L):
    """Takes in an element e and a sequence L to find it within the sequence"""
    if L==[] or L=='':
        return 0
    if L[0]==e:
        return 0
    else:
        return 1 + ind(e, L[1:])
#part D
def removeAll(e,L):
    """Takes in an element e and a list L to remove all the e's from that given list"""
    if L==[]:
        return []
    if L[0]==e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])
    
#part E

def even(X):
    if X % 2 == 0 : return True
    else: return False
    
def myFilter(f,L):
    if L==[]:
        return []
    if f(L[0])==True:
        return myFilter(f, L[1:])
    else:
        return [L[0]] + myFilter(f, L[1:])


def deepReverse(L):
    """Takes an input a list of elements and reverses them."""
    if L == []:
        return []
    if(isinstance(L[0],list)):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]

