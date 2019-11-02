'''
Given an array of strings print the max length string with unique chars that can be formed from the subset of the array.
Code Passes all the test case in LeetCode
T - O(nlogn + n^2)
S - O(n)
'''
def maxLength(arr)
        tmpar = [i for i in arr if len(i)==len(list(set(i)))]
        tmpar = sorted(tmpar, key = lambda x:len(x), reverse = 1)
        if tmpar==[]:
            return 0
        tmp = []
        for i in tmpar:
            count = len(i)
            st = i
            if count==0:
                continue
            for j in tmpar:
                if j==i:
                    continue
                if len(st+j)==len(list(set(st+j))):
                    count += len(j)
                    st = st+j
            tmp.append(count)
        return max(tmp)
    
