'''
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
'''


# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        
        #create the prefix sum of the array
        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]

        #check of 0 in prefix sum array
        if 0 in A:
            return 1
        
        #check if repeating characters in prefix sum array
        if len(set(A))!=len(A):
            return 1
        
        #not a zero
        return 0