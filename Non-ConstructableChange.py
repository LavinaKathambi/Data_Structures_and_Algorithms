'''
You are given an array
Return the minimum amount of change you cannot create 
ie. 
[1, 2, 5] = 4, as 4 cannot be created by any sum of no's in the array
'''

# O(n log n) Time | O(1) Space
def nonConstructibleChange(coins):
	# Sort the array in place 
	coins.sort()
	
	# Assign the current change to zero 
	minChange = 0 
	
	# Loop through array 
	for coin in coins:
		if coin > minChange + 1:
			return minChange + 1
		else:
			minChange += coin
		
    return minChange + 1

