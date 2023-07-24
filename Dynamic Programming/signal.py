'''
You are trying to send signals to aliens using a linear array of A laser lights. You don't know much about how the aliens are going to percieve the signals, but what you know is that if two consecutive lights are on then the aliens might take it as a sign of danger and destroy the earth.
Find and return the total number of ways in which you can send a signal without compromising the safty of the earth. Return the ans % 109 + 7.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #create a dynamic array to get the answer
        dynamic=[
            0
            for _ in range(A+1)
        ]
        dynamic[0]=1
        #since we can't have consecutive lights open
        dynamic[1]=2

        #iterate for each value in the dynamic array
        for index in range(2,A+1):
            dynamic[index]=(
                dynamic[index-1]+
                dynamic[index-2]
            )%1000000007
        
        #return the answer
        return dynamic[A]%1000000007
