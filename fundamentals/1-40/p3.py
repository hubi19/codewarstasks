def find_average(numbers):

    if len(numbers) < 1:

        return 0
    else:

        sum = 0
        count = 0

        for number in numbers:

            count += 1
            sum += number

        result = sum / count
        return result