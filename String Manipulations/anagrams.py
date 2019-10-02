'''
A function which returns the min no. of deletions to make two strings anagrams of each other.
Two strings are said anagrams either of them can be rearranged to get the other.
e.g. abcd and dbca are anagrams but abc and bcd aren't.

Reference - Hackerrank Practice Question (Passes all the test cases)

Time Complexity - 3*O(max(m,n))
Space Complexity - O(m)+O(n)
'''


def makeAnagram(a, b):
	'''
	Args : 
	a (str) - input string 1
	b (str)	- input string 2
	'''

    ls = len(a)
    lb = len(b)
    if ls>lb:
        small = b
        big = a
        tmp = ls
        ls = lb
        lb = tmp
    else:
        small = a
        big = b
    ds = {}
    db = {}
    for i in range(lb):
        if big[i] in db:
            db[big[i]]+=1
        else:
            db[big[i]] = 1
        if i<=ls-1:
            if small[i] in ds:
                ds[small[i]]+=1
            else:
                ds[small[i]]=1
    count = 0
    for i in db:
        if i in ds:
            if db[i]==ds[i]:
                continue
            else:
                count+=abs(db[i]-ds[i])
        else:
            count+=db[i]
    for i in ds:
        if i not in db:
            count+=ds[i]
    return count

