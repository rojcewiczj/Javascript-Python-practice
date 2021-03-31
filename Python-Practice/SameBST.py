def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
		return False
    
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	leftOne = getSmaller(arrayOne)
	print("leftOne: ",leftOne)
	leftTwo = getSmaller(arrayTwo)
	print("leftTwo: ", leftTwo)
	rightOne = getBiggerOrEqual(arrayOne)
	print("rightOne: ", rightOne)
	rightTwo = getBiggerOrEqual(arrayTwo)
	print("rightTwo ", rightTwo)
	
	return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo) 

def getSmaller(array):
	smaller = []
	for i in range(1, len(array)):
		if array[i] < array[0]:
			smaller.append(array[i])
	return smaller

def getBiggerOrEqual(array):
	biggerOrEqual = []
	for i in range(1, len(array)):
		if array[i] >= array[0]:
			biggerOrEqual.append(array[i])
	return biggerOrEqual