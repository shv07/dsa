'''
Passed all test cases g4g in 0.07 s. A code to
fllatten a linked list and return the sorted 
and flattened list's root node with nodes having
the the given structure

problem link - https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1 
'''




#This is a function problem.You only need to complete the function given below
#User function Template for python3
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''




def flatten(root):
    #Your code here
    tmp = root
    ar = []
    while tmp!=None:
        tmp1 = tmp
        while tmp1!=None:
            ar.append(tmp1.data)
            tmp1 = tmp1.bottom
        tmp = tmp.next
    ar.sort()
    root1 = Node(ar[0])
    tmp = root1
    for i in ar[1:]:
        tmp1 = Node(i)
        tmp.bottom = tmp1
        tmp = tmp.bottom
    return root1
