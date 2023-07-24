'''
Given a M x N grid A of integers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Return the minimum sum of the path.

NOTE: You can only move either down or right at any point in time.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):

        #get a dynamic array
        dynamic=[
            [float('inf')]*len(A[0])
            for _ in range(len(A))
        ]
        dynamic[0][0]=A[0][0]

        #write a recursion function to iterate throught the values
        def min_path(row,col):
            #base case
            if not row and not col:
                return dynamic[0][0]
            if row<0 or col<0:
                return float('inf')
            #check if value is in the dynamic array
            if dynamic[row][col]!=float('inf'):
                return dynamic[row][col]
            #else we would calculate the value
            else:
                #get the value
                dynamic[row][col]=min(
                    min_path(row-1,col),
                    min_path(row,col-1)
                )+A[row][col]
            #return the min 
            return dynamic[row][col]
        
        #return the answer
        return min_path(len(A)-1,len(A[0])-1)
