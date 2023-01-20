def positive_sum(arr):

    sum = 0

    for number in arr:
        if number >= 1:
            sum += number
    return sum
