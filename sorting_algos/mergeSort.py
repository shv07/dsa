def merge(a,b):
    if a == []:
        return b
    if b == []:
        return a
    i=0
    j=0
    l1 = len(a)
    l2 = len(b)
    ans = []
    while i<l1 and j<l2:
        if a[i]<=b[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            j+=1
    if i<l1:
        while i<l1:
            ans.append(a[i])
            i+=1
    elif j<l1:
        while j<l2:
            ans.append(b[j])
            j+=1
    else:
        pass
    return ans

def msort(a):
    l = len(a)
    if l<=1:
        return a
    mid = l//2
    a1 = msort(a[:mid])
    b = msort(a[mid:])
    return merge(a1,b)

