 def moveZeroes(nums):
    """
    Move all the occurence of zeros to end of the array without changing anyone's relative order.
    Do it inplace in O(n)
    Ref - Question taken from LeetCode
    """
    l = len(nums)
    zpos = 0
    nextnz = 1
    while zpos<l and nextnz<l:
        if nums[zpos]!=0:
            zpos+=1
            nextnz+=1
            continue
        if nums[nextnz]==0:
            nextnz+=1
        else:
            tmp = nums[zpos]
            nums[zpos] = nums[nextnz]
            nums[nextnz] = tmp
            zpos+=1
            nextnz+=1
            
