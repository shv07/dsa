'''
ref - https://leetcode.com/contest/weekly-contest-164/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/ 
Tags - LeetCode, Hard, Contest

Problem 1269. 

	Number of Ways to Stay in the Same Place After Some Steps
	User Accepted:782
	User Tried:1159
	Total Accepted:813
	Total Submissions:2727
	Difficulty:Hard
	You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should 		not be placed outside the array at any time).

	Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

	Since the answer may be too large, return it modulo 10^9 + 7.

Example:
	Input: steps = 3, arrLen = 2
	Output: 4
	Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
	Right, Left, Stay
	Stay, Right, Left
	Right, Stay, Left
	Stay, Stay, Stay

Complexities - S - O(nk), T - O(nk) [Each of the unique points at most is evaluated once and stored once in the dp array]

'''


def f(step, cur):
    
    global l
    global gstep
    
    if (step, cur) in dp:
        return dp[(step,cur)]
    if step==gstep:
        if cur==0:
            return 1
        return 0
    a = 0
    b = 0
    c = 0
    if cur>0:
        a = f(step+1, cur-1)
    if cur<l:
        b = f(step+1, cur+1)
    c = f(step+1,cur)
    dp[(step,cur)] = a+b+c
    return a+b+c
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        global l
        global gstep
        global dp
        dp = {}
        gstep = steps
        l = arrLen-1
        t = f(0,0)
        return t % ((10**9)+7)
        
