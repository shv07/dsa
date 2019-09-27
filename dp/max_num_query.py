'''
Descriptn
'''


a = [25,4,10,15,1,0,20,20]
q = [0,1,2,3,4,5,6,7]

def f(arr,q):
    n = len(arr)-1
    d = {n:1}
    prev_max = arr[n]
    frq = 1
    ans = []
    for i in range(n-1,-1,-1):
        if arr[i]==prev_max:
            frq+=1
            d[i] = frq
        elif arr[i]>prev_max:
            prev_max = arr[i]
            d[i] = 1
            frq = 1
        else:
            d[i] = frq
    res = []
    for i in q:
        res.append(d[i])
    return res
    
print(f(a,q))
