def countAndSay(n):
	"""
	LeetCode question link - https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
	
	The count-and-say sequence is the sequence of integers with the first five terms as following:

	1.     1
	2.     11
	3.     21
	4.     1211
	5.     111221
	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.

	Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number 		of digits in groups of the same digit.

	Note: Each term of the sequence of integers will be represented as a string.
	"""
	
    if n==1:
        return "1"
    num = "1"
    for i in range(n-1):
        num1 = ""
        count = {}
        l = len(num)
        for idx,j in enumerate(num):
            count[j] = 1 if j not in count else count[j]+1
            if idx+1 <l:
                if num[idx+1]!=j:
                    num1 = num1+str(count[j])+j
                    del(count[j])
        num = num1 + str(count[num[-1]])+num[-1]
    return num
