'''
As it is Tushar's Birthday on March 1st, he decided to throw a party to all his friends at TGI Fridays in Pune. Given are the eating capacity of each friend, filling capacity of each dish and cost of each dish. A friend is satisfied if the sum of the filling capacity of dishes he ate is equal to his capacity. Find the minimum cost such that all of Tushar's friends are satisfied (reached their eating capacity).

NOTE:
Each dish is supposed to be eaten by only one person. Sharing is not allowed.
Each friend can take any dish unlimited number of times.
There always exists a dish with filling capacity 1 so that a solution always exists.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def solve(self, A, B, C):

        #create a for loop for each friend
        answer=0

        #get the maximum of the array
        maxi=max(A)
    
        #dynamic array for storing value
        dynamic=[
            [-1]*(maxi+1)
            for _ in range(len(B))
        ]

        #write a recursive code to get the answer
        def min_cost(index,stomach):
            #base case
            if not stomach:
                return 0
            if index<0:
                return float('inf')
            #if value in dynamic
            if dynamic[index][stomach]!=-1:
                return dynamic[index][stomach]
            else:
                #get the value if stomach has enough space
                if B[index]<=stomach:
                    dynamic[index][stomach]=min(
                        min_cost(index-1,stomach),
                        min_cost(index,stomach-B[index])
                        +C[index]
                    )
                else:
                    dynamic[index][stomach]=min_cost(index-1,stomach)
            #return the answer
            return dynamic[index][stomach]
        
        #call the function to get all the values
        min_cost(len(B)-1,maxi)
        
        #get answers out of the dynamic array
        answer=0
        for value in A:
            answer=answer+min_cost(len(B)-1,value)
       
        return answer



