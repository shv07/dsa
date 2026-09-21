```
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

863. All Nodes Distance K in Binary Tree

Medium

Topics - graph

Companies - TrueFoundry

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    # O(n^2) soln
    def _lcs(self,root, node1, node2):
        if not root:
            return None
        
        if root==node1:
            return node1
        if root==node2:
            return node2

        left = self._lcs(root.left, node1, node2)
        right = self._lcs(root.right, node1, node2)
        if left and right:
            return root
        return left or right

    def _dfsNcount(self, root, counter):
        
        if root.left:
            counter[root.left.val]=counter[root.val]+1
            self._dfsNcount(root.left, counter)
        if root.right:
            counter[root.right.val]=counter[root.val]+1
            self._dfsNcount(root.right, counter)


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root.left and not root.right:
            return []

        result = []
        counter = defaultdict(int)
        root_ = root

        self._dfsNcount(root_, counter)
        print(counter)
        def dfs(root):
            lcs = self._lcs(root_, root, target)
            if abs(counter[lcs.val]-counter[target.val]) + abs(counter[lcs.val]-counter[root.val])==k:
                result.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root_)
        return result



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(n) soln
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        if not root.left and not root.right:
            return []
        
        parents = {}

        def dfs(node, parent):
            if not node:
                return 
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        # populate the parent nodes 
        dfs(root, None)

        result = []
        visited = set()
        def find_nodes(root, dist):
            if not root or root in visited:
                return
            visited.add(root)
            if dist==k:
                result.append(root.val)
                return
            for neighbor in (root.left, root.right, parents[root]):
                find_nodes(neighbor, dist+1)
        
        find_nodes(target, 0)
        return result 
            



################ BFS Solution ###################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        if not root.left and not root.right:
            return []
        
        parents = {}

        def dfs(node, parent):
            if not node:
                return 
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        # populate the parent nodes 
        dfs(root, None)

        result = []
        def find_nodes():
            visited = {target}
            queue = deque([(target, 0)])
            while queue:
                node, dist = queue.popleft()
                
                if dist==k:
                    result.append(node.val)
                    continue 

                for neighbor in (node.left, node.right, parents[node]):
                    if neighbor and neighbor not in visited:
                        queue.append((neighbor, dist+1))
                        visited.add(neighbor)
                

        
        find_nodes()
        return result 
            


        

        
