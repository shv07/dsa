```
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

```

class Solution:        
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recurs(i,j,m,n, pos, grid, target, path):
            if i>=m or j>=n or i<0 or j<0 or (i,j) in path or grid[i][j]!=target[pos]:
                return False

            if pos==len(target)-1:
                return True

            path.add((i,j))
            for p,q in [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]:
                r = recurs(p,q,m,n,pos+1, grid, target, path)
                if r:
                    break
            #dp[(i,j,pos)] = r
            
            path.remove((i,j))
            return r
        m,n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                res = recurs(i,j,m,n,0,board,word, set())
                if res:
                    return True
        return False

            
        
