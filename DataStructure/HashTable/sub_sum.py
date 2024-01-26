# my bad sln
# def subarray_sum(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return [i, i]
#         if i > 0:
#             sub_sum = nums[i]
#             # reversed_arr = reversed(nums[0:i-1])
#             for j in reversed(range(0, i, 1)):
#                 sub_sum += nums[j]
#                 if(sub_sum == target): 
#                     return [j, i]
#     return []
            
def subarray_sum(nums, target):
    sum_index = {0:-1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if sum_index.get(current_sum - target) is not None:
            starting_index = sum_index[current_sum - target] + 1
            return [starting_index, i]
        sum_index.setdefault(current_sum, i) 
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
