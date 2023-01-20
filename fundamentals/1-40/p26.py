def sum_two_smallest_numbers(numbers):

    sorting = sorted(numbers)

    sum = sorting[0] + sorting[1]

    return sum

print(sum_two_smallest_numbers([9, 2312, 23, 1, 4, 6]))