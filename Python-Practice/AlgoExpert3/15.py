def smallestDifference(arrayOne, arrayTwo):
	# sort arrayOne and arrayTwo
    # define array for returning
	# define current least difference
	arrayOne.sort()
	arrayTwo.sort()
	return_list = []
	i = 0
	j = 0
	least = float('inf')
	while( i < len(arrayOne) and j < len(arrayTwo)):
		difference = abs(arrayOne[i] - arrayTwo[j])
		if difference == 0:
			return [arrayOne[i], arrayTwo[j]]
		if( difference < least):
		  	least = difference
		  	return_list = [arrayOne[i], arrayTwo[j]]
		if arrayOne[i] < arrayTwo[j]:
	    	i += 1
		else:
			j += 1
    return return_list

