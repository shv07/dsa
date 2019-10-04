'''
A program to find the nth catalan no.
Nth Catalan No. refers to the no. of distinct bst that can be formed with n nodes.

Time Complexity - O(n^2)
Space Complexity - O(n)
'''

data = {}
def catalan(n):
    if n<=1:
        return 1
    if n in data:
        return data[n]
    cat = 0
    for i in range(1,n+1):
        cat+=catalan(i-1)*catalan(n-i)
    data[n]=cat
    return cat

ans = []
for _ in range(int(input().strip())):
    n = int(input().strip())
    ans.append(catalan(n))
for i in ans:
    print(i)
