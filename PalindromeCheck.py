'''
You are given a string, check if it's a valid palindrom
'''

# O(n^2) Time | O(n) Space
def isPalindrome(string):
	reversedString = ""
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string == reversedString

# O(N) Space-Time
def isPalindrome(string):
	# create a new array to append string 
	newArr = []
    
	for val in reversed(range(len(string))):
		newArr.append(string[val])
		
	if ''.join(newArr) == string:
		return True
	else:
		return False

# O(n) Time O(1) Space
def isPalindrome(string):
	left = 0 
	right = len(string) - 1
	
	# loop inwards 
	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True



	
		
	



	

