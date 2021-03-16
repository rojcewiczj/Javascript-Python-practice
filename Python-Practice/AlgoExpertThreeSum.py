def threeNumberSum(array, targetSum):
	output_array = []
    array.sort()
	for i in range(0, len(array)- 2):
		left = i + 1
		right = len(array) -1
		while left < right:
			if(array[i] + array[left] + array[right]) == targetSum:
				output_array.append([array[i], array[left], array[right]])
			    left += 1
				right -= 1
			elif (array[i] + array[left] + array[right]) < targetSum:
				left += 1
			else:
				right -= 1
				
	return output_array
				