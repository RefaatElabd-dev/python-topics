def find_max_min(myList):
    max_value = myList[0]
    min_value = myList[0]
    for item in myList:
        if item < min_value:
            min_value = item
        elif item > max_value:
            max_value = item
    return (max_value, min_value)
    


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""