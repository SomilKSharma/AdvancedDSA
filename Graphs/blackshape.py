'''
Given character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : list of strings
	# @return an integer
	def black(self, A):

        #cpnvert A to a list of list
        for index,string in enumerate(A):
            A[index]=list(string)

        #write a depth first search recursive function
        def dfs(row,col):
            #base case
            if (
                row<0 or row>=len(A) or
                col<0 or col>=len(A[0]) or
                A[row][col]=='O'
            ):
                return
            #else change the value and iterate to the neighbouring elements
            A[row][col]='O'
            #iterate to the neighbours
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
        
        #iterate for each 'X' and count
        black_shapes=0
        for row in range(len(A)):
            for col in range(len(A[0])):
                #check
                if A[row][col]=='X':
                    dfs(row,col)
                    black_shapes+=1
        
        #return the black shapes
        return black_shapes
