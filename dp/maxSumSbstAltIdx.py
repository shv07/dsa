'''
***
Question Link - https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
A function to return the max possible sum of subset of given array, arr, such that no indices in the subset are adjacent.
T - O(n)
S - O(n)
Type - DP
Algo - Maintain a n sized sum list, s, to store the max subset sum. s[i] - the max subset sum till index i (inclusive)
       base - return 0 is max(arr)<=0
'''


def maxSubsetSum(arr):
    if max(arr)<=0:
        return 0

    n = len(arr)
    s = [0]*n
    prev = -1
    for i in range(n):
        if arr[i]<=0:
            s[i]=s[prev] if prev!=-1 else 0
            continue
        if prev==-1:
            s[i]=arr[i]
            prev=i
            continue
        if prev==i-1:
            if arr[i]>arr[prev]:
                s[i]=max(s[prev]-arr[prev]+arr[i], s[prev-1]+arr[i]) if prev>=1 else s[prev]-arr[prev]+arr[i]
                prev=i
            else:
                if prev>=1:
                    if s[prev-1]+arr[i]>s[prev]:
                        s[i]=s[prev-1]+arr[i]
                        prev=i
                    else:
                        s[i]=s[prev]
                else:
                    s[i]=s[prev]
        else:
            s[i]=s[i-1]+arr[i]
            prev=i
    return s[n-1]

