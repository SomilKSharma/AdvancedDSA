'''
You are climbing a staircase and it takes A steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Return the number of distinct ways modulo 1000000007
'''

class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):

        #create a dynamic array and initialise two values
        dynamic=[
            0
            for _ in range(A+1)
        ]
        dynamic[0],dynamic[1]=1,1

        #iterate for all the values of the dynamic array
        for index in range(2,A+1):
            dynamic[index]=dynamic[index-1]%1000000007+dynamic[index-2]%1000000007
        
        #return the answer
        return dynamic[A]%1000000007