def bublle_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],  nums[j+1] = nums[j+1] , nums[j]
    return nums

if __name__ == "__main__":
    bublle_sort([2,5,3,5,7,0])