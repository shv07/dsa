#code

'''
A code to find the max sum of the lengths of the non-overlapping subarrays with 'K' as the max element.
Question from geeksforgeeks - https://practice.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays/0 
T - O(n)
S - O(1)
Technique used - 2 pointer logic
Passes all test cases in 0.03
'''
#code
def getMaxSum(ar, n, k):
    i = 0
    j = 0
    f = 0
    count=0
    tmpsum = 0
    while i<n and j<n:
        if ar[j]>k:
            if f==1:
                newsum = j-i
                if newsum>tmpsum:
                    count = count-tmpsum+newsum
                f=0
                tmpsum = 0
            j+=1
            i=j
            
        elif ar[j]==k:
            if f==1:
                newsum = j-i
                if newsum>tmpsum:
                    count=count-tmpsum+newsum
                    tmpsum = newsum
                    i=j
                    j+=1
                else:
                    i+=1
                    j+=1
                    tmpsum = 0
            else:
                f = 1
                j+=1
                tmpsum = 0
        else:
            j+=1
    if f == 1:
        newsum=n-i
        if newsum>tmpsum:
            count+=-tmpsum+newsum
    return count
    


################   Main   ##################
ans = []
for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    k = int(input())
    ans.append(getMaxSum(ar,n,k))
for i in ans:
    print(i)
                    
