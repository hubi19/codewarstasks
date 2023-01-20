def is_square(n):

    number = 0
    number_sqr = 0

    if n > 0:
        for number in range(n):

            number +=1
            number_sqr = number ** 2
            if number_sqr == n:
                return True
            elif number_sqr > n:
                return False
    elif n == 0:
        return True
    else:
        return False            

print(is_square(26))