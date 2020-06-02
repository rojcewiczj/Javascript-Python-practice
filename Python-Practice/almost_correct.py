def activityNotifications(expenditure, d):
    inc = 0
    sec_inc = 0
    exp = []
    count = d
    notification = 0
    while  inc  < len(expenditure) :
        if inc < count:
            exp.append(expenditure[inc])
            inc += 1
        elif inc == count:
            n = len(exp)
            exp.sort()
            if n % 2 == 0:
                median1 = exp[n// 2]
                median2 = exp[n// 2 -1]
                median = (median1 + median2) / 2
            else:
                median = exp[n // 2]
            
            if expenditure[count] / median >= 2:
                notification += 1

            exp = []
            sec_inc += 1
            inc = sec_inc
            count += 1
        
    return notification