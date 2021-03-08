def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
	blueShirtHeights.sort()
	backRow = []
	frontRow = []
	if(redShirtHeights[-1] > blueShirtHeights[-1]):
    	backRow = redShirtHeights
		frontRow = blueShirtHeights
	
	
	else:
		backRow = blueShirtHeights
		frontRow = redShirtHeights
	
	for i in range(0, len(backRow)):
		if backRow[i] <= frontRow[i]:
			return False
	
	
    return True