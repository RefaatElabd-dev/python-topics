def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums), 1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(bubble_sort([5, 2, 1, 4, 3]))