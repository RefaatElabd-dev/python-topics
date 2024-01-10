def b_search(x, list):
    low = 0
    high = len(list)
    mid = 0
    iteration = 0
    print(f"searching on {x} the list: {list} with count {len(list)}")
    while True:
        iteration += 1
        print(iteration)

        if(high <= low):
            print(f"x is not founded")
            break;
        
        mid = (low + high) // 2
        if( x == list[mid]):
            print(f"x index is: {mid}")
            break
        elif (x < list[mid]):
            high = mid - 1
        else:
            low = mid + 1


b_search(7, [1, 5, 6, 7, 8, 9, 20, 50, 60, 99])
b_search(99, [1, 5, 6, 7, 8, 9, 20, 50, 60, 99])
b_search(1, [1, 5, 6, 7, 8, 9, 20, 50, 60, 99])
b_search(15, [1, 5, 6, 7, 8, 9, 20, 50, 60, 99])