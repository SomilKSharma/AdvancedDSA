'''
Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). 
At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. 
Return the total number unique paths from (1, 1) to (n, m).

Note: An obstacle is marked as 1 and empty space is marked 0 respectively in the grid.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):

        #get a dynamic array
        dynamic=[
            [-1]*len(A[0])
            for _ in range(len(A))
        ]
        #edge case
        if A[0][0]:
            return 0
        dynamic[0][0]=1

        #create a recursive function to get the answer
        def find_paths(row,col):
            #base case
            if not row and not col:
                return 1
            elif row<0 or col<0 or A[row][col]:
                return 0
            #see if the value is in the dynamic array
            if dynamic[row][col]!=-1:
                return dynamic[row][col]
            #else we would have to calculate the answer
            else:
                #get the answer
                dynamic[row][col]=(
                    find_paths(row-1,col)+
                    find_paths(row,col-1)
                )       
            #return the answer
            return dynamic[row][col]

        #return the answer
        return find_paths(len(A)-1,len(A[0])-1) 
