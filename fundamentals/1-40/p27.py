def binary_array_to_number(arr):

    sum = 0

    power = -1

    reversed_arr = arr[::-1]

    for number in reversed_arr:

        power += 1
        if number == 1:

            sum += 2 ** power
    return sum





print(binary_array_to_number([1, 0, 0, 0 , 1, 1]))