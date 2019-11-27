from itertools import permutations

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    d = {}
    for i in s:
        d[i]=d[i]+1 if i in d else 1
    a = ''
    for i in d:
        a=a+i*int(d[i]/2)
    l = len(a)
    a_all = []
    perms = permutations(a)
    for i in perms:
        a_all.append(''.join(i))
    a_all_set = set(a_all)
    a_all=list(a_all_set)
    a_all.sort()
    
    for i in a_all:
        idx = set()
        ainv = i[::-1]
        pos=0
        flag=0
        for idx_,j in enumerate(s):
            if j==ainv[pos]:
                pos+=1
                idx.add(idx_)
            if pos>=l-1:
                flag=1
                break
        if i=='aeiou':
            print(ainv)
            print(idx)
            print(flag)
            print(l)
            print(pos)
        if flag==1:
            a_perm = ''
            for idx_,j in enumerate(s):
                if idx_ not in idx:
                    a_perm=a_perm+j
            if a_perm in a_all_set:
                #print("a_perm ",a_perm)
                #print("idx", idx)
                #print(ainv)
                #print("\n\n", a_all[:5])
                return i

    return ''
print(reverseShuffleMerge("aeiouuoiea"))
