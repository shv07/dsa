#code
#passed all test cases in geeksforgeeks
#credits - geeeksforgeeks (for question and logic)
#reference - https://www.geeksforgeeks.org/trapping-rain-water/
#time taken - 1.33s
#time taken in c++ - 0.34s
ans = []

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    count = 0
    
    leftmax = [0]*n
    rightmax = [0]*n
    
    leftmax[0] = ar[0]
    rightmax[n-1] = ar[n-1]
    for i in range(1,n):
        if ar[i]>leftmax[i-1]:
            leftmax[i] = ar[i]
        else:
            leftmax[i] = leftmax[i-1]
    
    for i in range(n-2,-1,-1):
        if ar[i]>rightmax[i+1]:
            rightmax[i] = ar[i]
        else:
            rightmax[i] = rightmax[i+1]
    for i in range(1,n-1):
        t = min(leftmax[i-1], rightmax[i+1])
        if t>=ar[i]:
            count += t-ar[i]
    ans.append(count)
for i in ans:
    print(i)
