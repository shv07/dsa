'''
A simple implementation of finding the diameter of an nary tree in Python using bfs.
Passes all test cases in Leetcode.
'''


from collections import deque
def farthestBFS(graph, tmp):
    visited = set() #stores list of nodes visited while bfs
    d = [0]*len(graph.keys()) #stores distance of nodes from tmp i.e. d[i] is the distance(i,tmp)
    q = deque() #bfs queue
    q.append(tmp)
    while len(q)>0:
        crnt = q.popleft()  #popleft - inbuilt queue pop
        visited.add(crnt)
        for i in graph[crnt]:
            if i not in visited:
                q.append(i)
                d[i]+=d[crnt]+1
    s = d.index(max(d))
    return [s,max(d)]


def treeDiameter(edges):
    l = len(edges)
    if l<2:
        return l
    graph = {} #stores the list of neigbours for all each node
    for i in edges:
        if i[0] in graph:
            graph[i[0]].add(i[1])
        else:
            graph[i[0]]={i[1]}
        if i[1] in graph:
            graph[i[1]].add(i[0])
        else:
            graph[i[1]]={i[0]}
    s,_ = farthestBFS(graph, edges[0][0])
    _,d = farthestBFS(graph, s)
    return d

