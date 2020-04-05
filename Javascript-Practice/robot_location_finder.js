function trackRobot(...steps) {
	x = 0
	y = 0
	location = [x, y]
	direction = "north"
	steps_count  = 0
	steps_max = steps.length 
	while (steps_count < steps_max ) {
		if(direction == "north"){
			location[1] += steps[steps_count]
			steps_count += 1
			direction = "east"
		}
		else if(direction == "east"){
			location[0] += steps[steps_count]
			steps_count +=1
			direction = "south"
		}
		else if(direction == "south"){
			location[1]-= steps[steps_count]
			steps_count +=1
			direction = "west"
		}
		else if (direction == "west"){
			location[0] -= steps[steps_count]
			steps_count += 1
			direction = "north"
		}
	}
	 return location
}

// given an array of numbers representing steps in four directions, the function trackRobot returns the final location in [x,y] format