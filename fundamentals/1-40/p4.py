def zero_fuel(distance_to_pump, mpg, fuel_left):

    how_far = fuel_left * mpg

    if how_far >= distance_to_pump:

        return True
    else:

        return False