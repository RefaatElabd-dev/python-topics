def insertion_sort(nums):
    for i in range(1, len(nums), 1):
        temp = nums[i]
        j = i - 1
        while nums[j] > temp and j > -1:
            nums[j], nums[j + 1] = temp, nums[j]
            j -= 1
    return nums