#Code to find the height of Binary Tree using BFS
#Passes all testcases in hackerrank
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           
'''
from collections import deque
def height(root):
    if root.left==None and root.right==None:
        return 0
    tmp = root
    q = deque()
    q.append(tmp)
    visited = set()
    d = {}
    prev = None
    while len(q)>0:
        cur = q.popleft()
        visited.add(cur)
        if prev==None:
            d[cur]=0
            prev=cur
        if cur.left and cur.left not in visited:
            q.append(cur.left)
            d[cur.left]=d[cur]+1
        if cur.right and cur.right not in visited:
            q.append(cur.right)
            d[cur.right]=d[cur]+1
        prev = cur
    return max(d.values())
