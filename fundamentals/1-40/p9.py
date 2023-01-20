def maps(a):

    new_array = []

    for number in a:

        doubled = number * 2

        new_array.append(doubled)

    return new_array

print(maps([1, 2, 3]))