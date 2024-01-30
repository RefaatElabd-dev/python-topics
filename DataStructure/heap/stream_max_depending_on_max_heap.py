from max_heap import MaxHeap

def stream_max(nums):
    if len(nums) <= 1:
        return nums
    max_heap = MaxHeap()
    max_value = nums[0]
    for val in nums:
        if max_value < val:
            max_value = val
        max_heap.insert(max_value)
    output = []
    for i in range(len(max_heap.heap)):
        output.insert(0, max_heap.remove())
    return output





test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')

