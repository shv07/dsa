#prints left view of the tree whose root is given
#passes the test cases in geeksforgeeks in 0.06s
#method level order traversal with array implementaiton of que
# T - O(n), Space - O(n+n)
#question for refernce - https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    q = []
    left = []
    q.append(root)
    q.append('$')
    front = 0
    l = 1
    f = 1
    while front<=l:
        a = q[front]
        front+=1
        if a!='$':
            if a.left:
                q.append(a.left)
                l+=1
            if a.right:
                q.append(a.right)
                l+=1
            if f == 1:
                left.append(a.data)
            f = 0
        else:
            f = 1
            if front<=l:
                if q[front]!='$':
                    q.append('$')
                    l+=1
    left = list(map(str, left))
    #print(front, l)
    print(' '.join(left), end = '')
