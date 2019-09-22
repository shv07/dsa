#hackerrank-practice problem - 
#https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


'''
You are given  queries. Each query is of the form two integers described below:
- 1 x : Insert x in your data structure.
- 2 y : Delete one occurence of y from your data structure, if present.
- 3 z : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array

Function Description

Complete the freqQuery function in the editor below. It must return an array of integers where each element is a  if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

freqQuery has the following parameter(s):

queries: a 2-d array of integers

sample:
Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1

output final - Return an array with the output: [0,1]
'''

'''
Time Complexity: 3*O(1)*q = O(q)
Space Complexity: O(n1)+O(n2) where n1 is the no. of distinct nos. entered and n2 is the no. of distinct frequencies
'''


def freqQuery(queries):
    d = {}
    f = {}
    ans = []
    for q in queries:
        if q[0]==1:
            if q[1] in d:
                f[d[q[1]]]-=1
                d[q[1]]+=1
                if d[q[1]] in f:
                    f[d[q[1]]]+=1
                else:
                    f[d[q[1]]]=1
            else:
                d[q[1]]=1
                if 1 in f:
                    f[1]+=1
                else:
                    f[1]=1
        elif q[0]==2:
            if q[1] in d:
                f[d[q[1]]]-=1
                d[q[1]]-=1
                if d[q[1]] in f:
                    f[d[q[1]]]+=1
                else:
                    f[d[q[1]]]=1
                if d[q[1]]==0:
                    d.pop(q[1])
        else:
            if q[1] in f:
                if f[q[1]]>0:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                ans.append(0)
    return ans
