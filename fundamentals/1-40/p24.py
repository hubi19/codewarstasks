def better_than_average(class_points, your_points):

    points_sum = 0

    amount_of_students = len(class_points)

    for point in class_points:
        
        points_sum += point
    
    average = points_sum / amount_of_students

    if average < your_points:
        return True
    else:
        return False
print(better_than_average([2,3], 5))