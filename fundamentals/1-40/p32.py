def find_next_square(sq):

    import math

    squared = 0

    root = math.sqrt(sq)
    if int(root + 0.5) ** 2 == sq:
        squared = math.sqrt(sq)
        squared += 1
        
    else:
        return -1
        

    return int(squared ** 2)

print(find_next_square(144))