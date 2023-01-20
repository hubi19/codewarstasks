def reverse_seq(n):

    list = []

    list.append(n)

    
    for i in range(1, n):
        n -= 1

        list.append(n)
    
    
    return list

print(reverse_seq(5))

    
