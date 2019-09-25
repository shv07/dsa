#code
def maxSum(ar,l):
    
    tmp = max(ar)
    if tmp<0:
        return tmp
        
    #l = len(ar)
    A = [0]*l
    if ar[0]<0:
        A[0]=0
    else:
        A[0]=ar[0]
    
    for i in range(1,l):
        s = A[i-1]+ar[i]
        if s<0:
            A[i]=0
        else:
            A[i]=s
    return max(A)

t = int(input().strip())
ans = []
for _ in range(t):
    n = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    ans.append(maxSum(ar,n))

for i in ans:
    print(i)
