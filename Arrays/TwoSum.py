def twoSum(nums, target):
	"""
	Returns the indices of the two elements in nums whose sum is target
	Runtime - O(n)
	"""
    tmp = set( nums)
    half = target//2
    #l = len(nums)
    if half*2==target and nums.count(half)>1:
        res=[]
        for i in range(len(nums)):
            if nums[i]==half:
                res.append(i)
        return [res[0], res[1]]
    for i in nums:
        if i==half:
            continue
        if target - i in tmp:
            return [nums.index(i), nums.index(target-i)]
                
