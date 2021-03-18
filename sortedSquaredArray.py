'''
You are to write a function that takes in a non-empty sorted array of integers
The goal is return an array with sorted Squares 
The array returned should be the same length as the initial array
'''

# O(n) Space-Time Complexity

def sortedSquaredArray(array):
    # initialize a new array where len = len(array) 
    newArr = [0] * len(array)

    # define my pointers
    left = 0
    right = len(array) - 1
    # Pointer at the end of the new array where I am going to begin inserting from
    insertLoc = len(newArr) - 1

    # Iterate through the array inwards 
    while left <= right:
        leftSquare = array[left] * array[left]
        rightSquare = array[right] * array[right]

        # Compare the squares
        if leftSquare >= rightSquare:
            newArr[insertLoc] = leftSquare
            insertLoc -= 1
            left += 1
        else:
            newArr[insertLoc] = rightSquare
            insertLoc -= 1
            right -= 1
    return newArr

arr1 = [1, 2, 3, 5, 6, 8, 9]
arr2 = [-10, -5, 0, 5, 10]

print(sortedSquaredArray(arr1))
print(sortedSquaredArray(arr2))

