#perform d left rotation on a given array and return the result
# e.g. arr = [1,2,3,4], d = 2
# result = [3,4,1,2]
# result passes all the test cases in hackerrank
'''
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''

def rotLeft(a, d):
    n = len(a)
    if n==1:
        return a
    if d == n:
        return a
    for _ in range(d):
        tmp = a.pop(0)
        a.append(tmp)
    return a


a = [1,2,3,4]
d = 2
print(rotLeft(a,d))
