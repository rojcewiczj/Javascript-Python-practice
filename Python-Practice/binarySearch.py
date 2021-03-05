# array = [4,5,6,7,1,2]

# left = 0
# right = len(array) -1 
# first_int = array[0]
# target = 1
# while(left <= right):
#     middle = (left + right) // 2
#     if(array[middle] == target):
#         print(middle)
    
#     if target > array[middle] and target > first_int:
#         left = middle +1
#     elif target > array[middle] and target < first_int:
#         right = middle -1
#     if target < array[middle] and target > first_int:
#         right = middle -1
#     elif 
    
  
    
left = []
right = []

left.append(1)
left.append(2)
while(len(left) >0 ):
    right.append(left.pop())

print(right.pop())
while(len(right) > 0 ):
    left.append(right.pop())

left.append(3)
while(len(left) >0 ):
    right.append(left.pop())

print(right.pop())