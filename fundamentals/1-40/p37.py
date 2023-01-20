def grow(arr):

    result = 1

    for i in arr:

        result = result * i
    
    return result

print(grow([3, 1, 2]))
