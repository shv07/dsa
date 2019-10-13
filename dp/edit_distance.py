#code
def ED(A,B,i,j):
    global d
    if (i,j) in d:
        return d[(i,j)]
    if i==j==0:
        if A[i]==B[j]:
            d[(i,j)]=0
            return 0
        d[(i,j)]=1
        return 1
    if i==j==-1:
        return 0
    if i==-1:
        d[(i,j)] = j
        return j
    if j==-1:
        d[(i,j)] = i
        return i
    a = 1 + ED(A,B,i-1,j)
    b = 1 + ED(A,B,i,j-1)
    f = None
    if A[i]==B[j]:
        f = 0
    else:
        f = 1
    c = f + ED(A,B,i-1,j-1)
    d[(i,j)] = min(a,b,c)
    return d[(i,j)]

ans = []
for _ in range(int(input())):
    global d
    d = {}
    i,j = [int(t) for t in input().split()]
    A,B = input().split()
    ans.append(ED(A,B,i-1,j-1))
for i in ans:
    print(i)
