'''
You are given a function that takes in two parameters:
1. An Array
2. A sum
The goal is to find two numbers in the array that add up to the sum
You are to return an array of these 2 numbers and an empty array if otherwise
NB: Assume there will be at most a pair that makes this sum
'''

# Solution 1 Brute Force 
# O(n^2) time and O(n) Space
def twoNumberSum(array, targetSum):
    # define two pointers i, j
	i = 0
	j = i + 1
	newList = []
    # use a for loop to sum i to every j and append to a new list
	for i in array:
		for j in array:
			if i != j and i + j == targetSum:
				newList.append(i)
				newList.append(j)
				return newList
	return []

# Solution 2 Optimized Space 
# O(n^2) time and O(1) Space
def twoNumberSum(array, targetSum):
    # use a for loop to sum i to every j without appending to a new list
	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			if array[i] != array[j] and array[i] + array[j] == targetSum:
				return [array[i], array[j]]
	return []

# Solution 3 Optimized Space 
# O(n log n) time and O(1) space
def twoNumberSum(array, targetSum):
	array.sort()
	# define 2 pointers
	left = 0
	right = len(array)-1
	# sum up the leftmost and rightmost pointers and move accordingly
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			return [array[left], array[right]]
		elif currentSum < targetSum:
			left += 1
		elif currentSum > targetSum:
			right -= 1
	return []
	

# Solution 4 Optimized time 
# O(n) time and O(n) Space
def twoNumberSum(array, targetSum):
	# define a hash_table = dictionary
	my_dict = {}
	# loop through the array
	for num in array:
		if targetSum - num in my_dict:
			return [num, targetSum - num]
		else:
			# add the value to the dictonary 
			my_dict[num] = True
	return []

