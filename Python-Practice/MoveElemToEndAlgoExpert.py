def moveElementToEnd(array, toMove):
    left = 0
	right = len(array) -1
	
	while(left < right):
		
		while array[left] != toMove and left < right:
			left += 1
		while array[right] == toMove and right > left:
			right -= 1
		
		temp = array[right]
		array[right] = array[left]
		array[left] = temp
		print(left, right)
		print(array)
	   
		
		
    return array