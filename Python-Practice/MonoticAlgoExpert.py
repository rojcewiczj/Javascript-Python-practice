def isMonotonic(array):
	j = 0
	while(j < len(array)-1 and array[j] == array[j+1]):
		j += 1
	if j == len(array) -1:
		return True
	elif len(array) > 0:
		if array[j] < array[j+1]:
			up = True
		else:
			up = False
	
	for i in range(j, len(array)-1):
		if up == True and array[i] > array[i+1]:
			return False
		if up == False and array[i] < array[i+1]:
			return False
		
    return True