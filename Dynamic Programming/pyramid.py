'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Adjacent numbers for jth column of ith row is jth and (j+1)th column of (i + 1)th row
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):

        #create a dynamic array
        dynamic=[]
        for index in range(len(A)):
            dynamic.append(
                [float('inf')]*len(A[index])
            )
        
        #iterate for each value in the array to get the answer
        def min_path_sum(row,col):
            #base case at the last row
            if row==len(A)-1:
                dynamic[row][col]=A[row][col]
                return dynamic[row][col]
            #else check if value in the dynamic
            if dynamic[row][col]!=float('inf'):
                return dynamic[row][col]
            #else we have to calculte the answer
            else:
                dynamic[row][col]=min(
                    min_path_sum(row+1,col),
                    min_path_sum(row+1,col+1)               
                )+A[row][col]
            #return the value
            return dynamic[row][col]
        
        #get the answer
        return min_path_sum(0,0)

