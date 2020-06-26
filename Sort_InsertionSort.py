def Insertion_sort(nums):
    for i in range(len(nums) -1):
        j = i+1

        while j > 0 and nums[j] < nums[j-1]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j = j-1
    return nums

Insertion_sort([2,7,3,20,4,6])