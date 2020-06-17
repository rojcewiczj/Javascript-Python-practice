def activityNotifications(expenditure, d):
    array = [12,23,34,66,67]
    middle = len(array) // 2
    target = 67
    inc = 0
    while len(array) > 1:
        
        if target > array[middle]:
            array = array[middle:]
            middle = len(array) // 2
            inc += middle
        else:

            array = array[:middle]
            middle = len(array) // 2
            inc += middle 