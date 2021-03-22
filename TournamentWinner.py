'''
Tournament Winner:
There's a tournament, and teams go head to head, a function takes in 2 arrays as input
1. list of lists of which teams go against each other 
2. an array that has the results 
The len of both arrays are equeal hence, indexes correspond to each other 
The goal is to find the winning team 
Competitions  array represents = [homeTeam, awayTeam]
If 1 in results array, homeTeam won, if 0, awayTeam won 
'''

# O(N) Time | O(K) Space
def tournamentWinner(competitions, results):
	currentBestTeam = "" # winner so far
	scores =  {currentBestTeam:0}
	

	# loop through both arrays at the same time and keep track of results 
	for indx, competition in enumerate(competitions):
		result = results[indx]

		homeTeam, awayTeam = competition

		if result == 1:
			winningTeam = homeTeam
		else:
			winningTeam = awayTeam

	
		# define another function to update scores in the hash table 
		def scoresUpdate(teamName, pointsScored, scores):
			if teamName not in scores:
				scores[teamName] = 0

			# add the points scored so far
			scores[teamName] += pointsScored

		scoresUpdate(winningTeam, 3, scores)

		# check the current Best Team 
		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
	
	return currentBestTeam



arr = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
resultz = [0, 0, 1]
print(tournamentWinner(arr, resultz))




