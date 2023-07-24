'''
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
Also given an integer C which represents knapsack capacity.
Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE:
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        #create a dynamic array
        dynamic=[
            [-1]*(C+1)
            for _ in range(len(A))
        ]

        #create a recursive solution for the question
        def knapsack(index,weight):
            #base case of the recursive function
            if index<0 or weight<=0:
                return 0
            #check for value in the dynamic array
            if dynamic[index][weight]!=-1:
                return dynamic[index][weight]
            else:
                #calculate the value
                if weight>=B[index]:
                    dynamic[index][weight]=max(
                        knapsack(index-1,weight),
                        knapsack(index-1,weight-B[index])+A[index]
                    )
                else:
                    dynamic[index][weight]=knapsack(index-1,weight)
            #return the value
            return dynamic[index][weight]
        
        #return the answer
        return knapsack(len(A)-1,C)
