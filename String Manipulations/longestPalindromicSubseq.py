#code
#to return the longest possible palindromic sequence in a given string
#T - O(n^2), S - O(1)
#passes all the test cases in geeksforgeeks in 0.03 s
#ques link - https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0 

def longest(s):
    '''
    Args:
    s (str) - input string
    return:
    string (str) - longest palindromic substring
    '''

    l = len(s)
    string = ''
    prevl = 0
    for i in range(l-1):
        for j in range(i+1,l):
            if s[i:j+1]==(s[j:i-1:-1] if i!=0 else s[j::-1]):
                newl = j-i+1
                if newl>prevl:
                    prevl = newl
                    string = s[i:j+1]
                
    return string if prevl!=0 else s[0]
ans = []
for _ in range(int(input())):
    s = input()
    ans.append(longest(s))
for i in ans:
    print(i)
    
    
