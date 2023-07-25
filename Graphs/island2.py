'''
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a side with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.

(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.

(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.

(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.

Return the number of islands.

'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        #do a depth first search
        def dfs_island(row,col):
            #check the node is valid or not
            if (
                row<0 or row>=len(A) or
                col<0 or col>=len(A[0]) or
                not A[row][col]
            ):
                return
            #else we would iterate for the other elements
            A[row][col]=0
            dfs_island(row-1,col)
            dfs_island(row+1,col)
            dfs_island(row,col-1)
            dfs_island(row,col+1)
        
        #get an island counter
        island=0
        for row in range(len(A)):
            for col in range(len(A[0])):
                #call the dfs and increment the island counter
                if A[row][col]:
                    dfs_island(row,col)
                    island+=1
        
        #return the answer
        return island
