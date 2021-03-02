def tournamentWinner(competitions, results):
	
    teams = {}
	res = {0: 1, 1: 0}
	winning_score = 0
	winner = ""
	
	for i in range(0, len( results)):
	
		team = competitions[i][res[results[i]]]
		
		if team not in teams:
			teams[team] = 3
		else:
			teams[team] += 3
			
		if teams[team] > winning_score:
			winning_score = teams[team]
			winner = team
	
    return winner