def longest_consecutive_sequence(arr):
    cumulatives = {}
    max_seq = 0
    for i in sorted(arr):
        if cumulatives.get(i - 1):
            cumulatives[i] = cumulatives[i-1] + 1
        else:
            cumulatives[i] = 1
        max_seq = max(cumulatives[i], max_seq)
    return max_seq

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""