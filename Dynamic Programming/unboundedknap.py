'''
Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could fit in this quantity.
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):

        #get a dynamic array to store the value
        dynamic=[
            [-1]*(A+1)
            for _ in range(len(B))
        ]

        #write a recursive function to get the answer
        def knapsack(index,weight):
            #base case of the recursive function
            if index<0 or weight<=0:
                return 0
            #check if value in the dynamic array
            if dynamic[index][weight]!=-1:
                return dynamic[index][weight]
            #else we would get the answer 
            else:
                #check for the weight
                if weight>=C[index]:
                    dynamic[index][weight]=max(
                        knapsack(index-1,weight),
                        knapsack(index,weight-C[index])+B[index]
                    )
                else:
                    dynamic[index][weight]=knapsack(index-1,weight)
            #return the calculated answer
            return dynamic[index][weight]
        
        #return the answer
        return knapsack(len(B)-1,A)