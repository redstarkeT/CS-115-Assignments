'''
Created on 2/20/2020
@author:   Timothy Stephens
Pledge:    I pledge that I have abided by the Stevens Honor System.
CS115 - Lab4
'''

def knapsack(capacity, itemList):
    """Takes in a maximum weight,capacity, and a list of lists, [weight,value],
    returning [highest value, [item1weight,item1val],[item2weight,item2val]]"""
    if itemList==[]:
        return [0,[]]
    if capacity==0:
        return [0,[]]
    if itemList[0][0] > capacity:
        return knapsack(capacity,itemList[1:])
    else:
        use=knapsack(capacity-itemList[0][0],itemList[1:])
        lose=knapsack(capacity,itemList[1:])
        StarPlatinum=[itemList[0][1]+use[0],[itemList[0]]+use[1]]
        if StarPlatinum[0] > lose[0]:
            return StarPlatinum
        else:
            return lose
                    
                      
        
        
