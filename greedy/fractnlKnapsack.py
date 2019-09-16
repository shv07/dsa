#returns the maximum value of fractional knapsack of capacity C, with given N values and weights 
#checked(passed) on geeksforgeeks test cases
def fracKnapsack(Data,C,N):
    '''
    Args:
    Data - N x 3 array [....,[v_i, w_i, d_i],.....]
	   v_i - value of item i, w_i - weight of item i, d_i - weight of item i
    C - maximum weight capacity of knapsack
    N - Total no of available items
    '''
    sack = []
    count = 0
    D_sorted = sorted(Data, key = lambda x:x[2], reverse = 1)
    
    f = 0.0000
    for e in D_sorted:
        if count + e[1]==C:
            count+=e[1]
            sack.append(e[0])
            break
        if count + e[1]>C:
            f = ((C-count)*e[0])/e[1]
            break
        count+=e[1]
        sack.append(e[0])
    sack_ = sum(sack) + f +0.000000
    return round(sack_,2)



T = int(input())
res = []
for _ in range(T):
    N,C = [int(i) for i in input().strip().split()]
    tmp = [int(i) for i in input().strip().split()]  # 2*N space seperated values corresponding to v_i, w_i
    Data = [[tmp[2*i],tmp[2*i+1],(tmp[2*i]/tmp[2*i+1])] for i in range(N)]
    res.append(fracKnapsack(Data,C,N))
for i in res:
    print(i)
