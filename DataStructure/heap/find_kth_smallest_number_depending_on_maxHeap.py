from max_heap import MaxHeap

def find_kth_smallest(nums, k):
    if nums is None or k is None or len(nums) <= k:
        return None
    max_heap = MaxHeap()
    for val in nums:
        max_heap.insert(val)
    for i in range(len(max_heap.heap) - k):
        max_heap.remove()
    return max_heap.heap[0]