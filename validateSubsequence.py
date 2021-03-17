'''
You are given two non-empty arrays
A and B, check if B is a valid subsequence of A
'''

# O(N) Time | O(1) Space
def isValidSubsequence(array, sequence):
    # define 2 pointers 
    arr_pointer = 0
    seq_pointer = 0

    # check that the pointers don't go beyond the length of the arrays
    while arr_pointer < len(array) and seq_pointer < len(sequence):
        # compare elements in both arrays 
        if array[arr_pointer] == sequence[seq_pointer]:
            seq_pointer += 1
        arr_pointer += 1

    # Check if valid subsequence, if traveresed entire subsequence
    if seq_pointer == len(sequence):
        return True
    return False


main_array = [5, 1, 22, 25, 6, -1, 8, 10]
sub_array = [1, 6, -1, 10]

print(isValidSubsequence(main_array, sub_array))
