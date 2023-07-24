'''
Given a 2 x N grid of integers, A, your task is to choose numbers from the grid such that sum of these numbers is maximized. 
However, you cannot choose two numbers that are adjacent horizontally, vertically, or diagonally. 

Return the maximum possible sum.

Note: You are allowed to choose more than 2 numbers from the grid.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def adjacent(self, A):

        #create a new array with max of each row in a 1-D array
        array=[]
        #iterate for the values in the array
        for index in range(len(A[0])):
            array.append(max(A[0][index],A[1][index]))

        #edge case
        if len(array)==1:
            return array[0]
        
        #create a dynamic array
        dynamic=[
            None
            for _ in range(len(array))
        ]
        dynamic[0]=array[0]
        dynamic[1]=max(array[0],array[1])

        #iterate for each value in the array
        def max_sum(index):
            #base case
            if index in [0,1]:
                return dynamic[index]
            #check if value in the dynamic array
            if dynamic[index]:
                return dynamic[index]
            #else we would calculate the value
            else:
                #get the value
                dynamic[index]=max(
                    max_sum(index-2)+array[index],
                    max_sum(index-1)
                )
            #return the value
            return dynamic[index]
        
        #store the value in an answer variable
        answer=max_sum(len(array)-1)
        
        #return the answer
        return answer




