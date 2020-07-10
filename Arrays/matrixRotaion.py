def rotate(matrix):
    """
    Rotatate the n x n matrix clockwise by 90 degree in-place.
    question link - https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
    Time - O(n**2) = O(size of matrix)
    Space - O(n**2)
    """
    n = len(matrix)-1
    seen = set()
    for i in range(n+1):
        for j in range(n+1):
            if (i,j) in seen:
                continue
            t1 = matrix[i][j]
            
            matrix[i][j] = matrix[n-j][i]
            matrix[n-j][i] = matrix[n-i][n-j]
            matrix[n-i][n-j] = matrix[j][n-i]
            matrix[j][n-i] = t1
            
            seen.add((i,j))
            seen.add((n-j,i))
            seen.add((n-i,n-j))
            seen.add((j,n-i))
    
    
