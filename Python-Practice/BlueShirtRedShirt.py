def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    sorted_redShirt = sorted(redShirtSpeeds)
	sorted_blueShirt = sorted(blueShirtSpeeds)
	print(sorted_redShirt)
	print(sorted_blueShirt)
    total_speed = 0
	if fastest == True:
		j = len(redShirtSpeeds) - 1
		endStart = True
	else:
		j = 0
		endStart = False
	i = 0
	while  i < len(redShirtSpeeds):
		redShirt = sorted_redShirt[i]
		blueShirt = sorted_blueShirt[j]
		total_speed += max(redShirt, blueShirt)
		if endStart == True:
			j -= 1
		else:
			j += 1
		i += 1
		
	   

		
	print(total_speed)
				
				
    return total_speed