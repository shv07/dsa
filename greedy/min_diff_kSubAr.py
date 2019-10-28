'''
************************************important question*********************************
Function to return k length subset of array such that the max-min of the subset is minimum possible for the given array
question link - https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

T - O(nlogn+n-k)
S - O(1)

Technique - Greedy with array manipulation

Algorithm - sort the array. initialise the required boundary indices as 0 and k-1. iterate from n-k times and increment boundaries by 1 as that gives the minimum possible min-max for tha starting or the ending element with k size subset. Keep checking the difference to previous minimum and update if less than the previous.
'''

def maxMin(k, arr):
	'''
	Args:
		k (int) - required subset size
		arr (list) - given array
	Return:
		d (int) - minm possible diff. for max and min
	'''
	
    n = len(arr)
    
    #consider entire array if k==n
    if k==n: 
        return max(arr)-min(arr)
    
    arr.sort()
    
	#ns - new start index
	#ne - new end index
    start=ns=0
    end=ne=k-1
    while ne<n:
        if arr[ne]-arr[ns]<arr[end]-arr[start]:
            start=ns
            end=ne
        ns+=1
        ne+=1
    return arr[end]-arr[start]

