'''
There is a rectangle with left bottom as (0, 0) and right up as (x, y).

There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @param E : list of integers
	# @param F : list of integers
	# @return a strings
	def solve(self, A, B, C, D, E, F):

        #create an array with the give information
        array=[
            [0]*(B+1)
            for _ in range(A+1)
        ]

        #iterate for all the points in the array E and F
        for index in range(C):
            #get the x and the y coordinate
            x=E[index]
            y=F[index]
            #iterate for all the points in the array to mark 1 if under circle
            for row in range(A+1):
                for col in range(B+1):
                    #check
                    if ((x-row)**2+(y-col)**2)**0.5<=D:
                        array[row][col]=1
        
        #check if start or end is under the circle
        if array[0][0] or array[A][B]:
            return 'NO'

        #write the depth first search algorithm
        def dfs(row,col):
            #check for the edge cases
            if (
                row<0 or row>=A+1 or
                col<0 or col>=B+1 or
                array[row][col]==1
            ):
                return
            #else iterate for the elements
            array[row][col]=1
            dfs(row+1,col+1)
            dfs(row+1,col-1)
            dfs(row-1,col+1)
            dfs(row-1,col-1)
            dfs(row,col+1)
            dfs(row,col-1)
            dfs(row+1,col)
            dfs(row-1,col)
        
        #call the function
        dfs(0,0)

        #return the answer
        if array[A][B]:
            return 'YES'
        return 'NO'
