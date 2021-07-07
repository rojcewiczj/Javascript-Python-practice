

def find():
    lost = 0
    array_of_stuff = [1,2,3,4,5]

    for num in array_of_stuff:
        if num == 1:
            lost += num
    
    return lost

print(find())
