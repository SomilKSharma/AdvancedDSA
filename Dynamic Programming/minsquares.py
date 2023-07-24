'''
Given an integer A. Return minimum count of numbers, 
sum of whose squares is equal to A.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, A):

        #create a dynamic array and fill the first two values
        dynamic=[
            -1
            for _ in range(A+1)
        ]
        dynamic[0],dynamic[1]=0,1

        #write a recursive function to get the answer
        def min_count_sq(number):
            #base case
            if number in [0,1]:
                return number
            #check if value in dynamic array
            if dynamic[number]!=-1:
                return dynamic[number]
            #else calculate the value
            else:
                #create a minimum value 
                minimum=float('inf')
                #iterate for all the squares less than the number
                sqr=1
                while sqr*sqr<=number:
                    #get the minimum values
                    minimum=min(
                        minimum,
                        min_count_sq(number-sqr*sqr)+1
                    )
                    #iterate the square further
                    sqr=sqr+1
                #store the value in the dynamic array
                dynamic[number]=minimum
            #return the value
            return dynamic[number]
        
        #get the answer
        answer=min_count_sq(A)

        #return the answer
        return answer


