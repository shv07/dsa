'''
Function to find the pair in array with minimum abs difference
T - O(nlogn + n)
S - O(1)
Method - Greedy
Idea - Once you have sorted the array, for any given no. the smallest difference for it can only come from subtracting it with its adjacent no. All other nos. will have larger diff. value.
'''

def minimumAbsoluteDifference(arr):
	'''
	Args:
	arr (list) - Required Array
	Return:
	minm (int) - the minimum abs. diff.
	'''
	
    n = len(arr)

    #return 0 if any duplicate element found
    if n!=len(list(set(arr))):
        return 0

    arr.sort()
    minm = float('inf')
    for i in range(n-1):
        tmp = abs(arr[i]-arr[i+1])
        if tmp<minm:
            minm=tmp
    assert(minm!=float('inf'))
    return minm

