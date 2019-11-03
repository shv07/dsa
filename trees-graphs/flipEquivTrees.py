'''
A program to check weather 2 given trees are flip equivalent.
T - O(m+n)
S - O(n)
Algo - BFS Modification - checks if node values are equal. if yes checks for the left and right child else return No.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1==None and root2==None:
            return 1
        if root1==None or root2==None:
            return 0
        q1,q2 = deque(), deque()
        q1.append(root1)
        q2.append(root2)
        while len(q1)>0 and len(q2)>0:
            n1 = q1.popleft()
            n2 = q2.popleft()
            if n1.val!=n2.val:
                return 0
            if n1.left and n1.right:
                
                if n2.left==None or n2.right==None:
                    return 0
                if n1.left.val==n2.left.val and n1.right.val==n2.right.val:
                    pass
                else:
                    tmp = n1.left
                    n1.left = n1.right
                    n1.right = tmp
                    del(tmp)
            elif n1.left:
                if n2.left==None:
                    if n2.right==None:
                        return 0
                    n1.right=n1.left
                    n1.left=None
                else:
                    if n2.right:
                        return 0
            elif n1.right:
                if n2.right==None:
                    if n2.left==None:
                        return 0
                    n1.left=n1.right
                    n1.right=None
                else:
                    if n2.left:
                        return 0
            elif n1.left==None and n1.right==None:
                if n2.left!=None or n2.right!=None:
                    return 0
            else:
                pass
            if n1.left:
                q1.append(n1.left)
            if n1.right:
                q1.append(n1.right)
            if n2.left:
                q2.append(n2.left)
            if n2.right:
                q2.append(n2.right)
        if len(q1)>0 or len(q2)>0:
            return 0
        return 1
                
                    
            
