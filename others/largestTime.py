'''
Given a 4 integer array, find the largest time in 24 hour format that can be made using them
'''
def isValid(x):
    if len(x)<4:
        return 0
    if x[0]>'2':
        return 0
    if x[0]=='2':
        if x[1]>'3':
            return 0
    if x[2]>'5':
        return 0
    return 1
    
def largestTimeFromDigits(self, A: List[int]) -> str:
	tmp = A
	if 0 not in tmp and 1 not in tmp and 2 not in tmp:
	    return ""
	ans = '-1'
	for i in range(4):
	    for j in range(4):
		if j==i:    continue
		for k in range(4):
		    if k==i or k==j:    continue
		    for l in range(4):
		        if l==k or l==j or l==i:    continue 
		        if i not in [j,k,l] and j not in [k,l] and k!=l:
		            x = (''.join(map(str,[A[i],A[j],A[k],A[l]])))
		            if x>ans:
		                if isValid(x):
		                    ans=x
	if isValid(ans):
	    return ans[:2]+":"+ans[2:]
	return ""
		            
