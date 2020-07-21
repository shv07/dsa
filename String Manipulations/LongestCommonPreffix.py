def longestCommonPrefix(strs):
	"""
	longest common prefix among the list of strigs, strs
	T - O(mn), m- len of longest common prefix and n-len of the list
	"""
    l = len(strs)
    if l==0:
        return ""
    if l==1:
        return strs[0]
    if len(strs[0])==0:
        return ""
    
    i,j=0,0
    ans = strs[0][0]
    while True:
        if j==l:
            j=0
            i+=1
            if len(strs[j])<i+1:
                ans = ans[:i]
                break
            ans = ans+strs[j][i]
        if len(strs[j])<i+1:
            ans = ans[:i]
            break
        if strs[j][i]==ans[i]:
            j+=1
        else:
            ans = ans[:i]
            break
    return ans
