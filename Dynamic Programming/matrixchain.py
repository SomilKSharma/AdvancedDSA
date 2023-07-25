'''
Given an array of integers A representing chain of 2-D matices such that the dimensions of ith matrix is A[i-1] x A[i].

Find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.
Return the minimum number of multiplications needed to multiply the chain.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #create the dynamic array
        dynamic=[
            [float('inf')]*len(A)
            for _ in range(len(A))
        ]

        #write the recursive function to get the answer
        def min_multi(start,end):
            #base case
            if start==end:
                return 0
            #check if value is in the dynamic array
            if dynamic[start][end]!=float('inf'):
                return dynamic[start][end]
            else:
                #calculate the value of the same
                mini=float('inf')
                #iterate for all ranges in the start and end
                for index in range(start,end):
                    #get the minimum value
                    mini=min(
                        mini,
                        min_multi(start,index)+min_multi(index+1,end)+(A[start-1]*A[index]*A[end])
                    )
                #put the value in the dynamic array
                dynamic[start][end]=mini
            #return the value
            return dynamic[start][end]
        
        #return the answer
        return min_multi(1,len(A)-1)
        
