"""
Given the no. of steps in a staircase, find the no. of ways you can reach to the top, starting from the bottom.
You can climb 1 or 2 steps at a time.
T - O(log n) roughly
S - O(n) 
Ref - LeetCode - https://leetcode.com/submissions/detail/372829559/?from=/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/569/
"""
dp = None
def num(i,n):
    global dp
    if i in dp:
        return dp[i]
    
    if i==n-1:
        dp[i]=1
        return 1
    if i==n-2:
        dp[i]=2
        return 2
    if i==n:
        return 0
    tmp = num(i+1,n)+num(i+2,n)
    dp[i]=tmp
    return tmp
def climbStairs(n):
    global dp
    dp={}
    i=0
    return num(i,n)
