def Selection_sort(nums):
    for i in range(len(nums) - 1):
        index_min = i
        for j in range(i, len(nums)):
            if nums[j]< nums[index_min]:
                index_min = j
        if index_min != i:
            nums[i], nums[index_min] = nums[index_min],nums[i]
    
    return nums

Selection_sort([3,25,4,7,10])