def find_pairs(arr1, arr2, target):
    output = []
    arr1_as_set = set(arr1)
    for num in arr2:
        if (target - num) in arr1_as_set:
            output.append((target - num, num))
    return output



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""