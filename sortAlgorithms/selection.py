def selection_sort(nums):
    for i in range(0, len(nums), 1):
        min_index = i
        for j in range(i + 1, len(nums), 1):
            if(nums[min_index] > nums[j]):
                min_index = j
        if(min_index != i):
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selection_sort([4,2,6,5,1,3]))