def activityNotifications(expenditure, d):
    totals = {}
    for num in range(0, d):
        totals[num] = 0
    inc = 0
    def insert(inc, index):
        totals[inc] += expenditure[index]
        if inc > 0:
            insert(inc - 1, index)
        
    

        


    for index, element in enumerate(expenditure):
        if index > 0:
            inc += 1
        insert(inc, index)
    


  
    print(totals)