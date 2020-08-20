def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  allPoss = []
  if n == 0:
    return [[]]
    
  def roundChoice(round, roundNumber):
      for i in range(len(options)):
          round.append(options[i])
          print(round)
          print(roundNumber)
          if roundNumber == n :
            allPoss.append(round)
          else:
            roundChoice(round, roundNumber + 1)
          round.pop()
  roundChoice([], 1 )
 
 
rock_paper_scissors(4)