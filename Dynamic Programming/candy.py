'''
Rishik likes candies a lot. So, he went to a candy-shop to buy candies.
The shopkeeper showed him N packets each containg A[i] candies for cost of C[i] nibbles, each candy in that packet has a sweetness B[i]. The shopkeeper puts the condition that Rishik can buy as many complete candy-packets as he wants but he can't buy a part of the packet.
Rishik has D nibbles, can you tell him the maximum amount of sweetness he can get from candy-packets he will buy?
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        #create a dynamic array to get the answer
        dynamic=[
            [-1]*(D+1)
            for _ in range(len(A))
        ]

        #write a recursived function to get the answer
        def candies(index,nibbles):
            #base case
            if index<0 or nibbles<=0:
                return 0
            #check if value in the dynamic array
            if dynamic[index][nibbles]!=-1:
                return dynamic[index][nibbles]
            #else we will calculate the value
            else:
                #check for the cost
                if nibbles>=C[index]:
                    dynamic[index][nibbles]=max(
                        candies(index-1,nibbles),
                        candies(index,nibbles-C[index])+B[index]*A[index]
                    )
                else:
                    dynamic[index][nibbles]=candies(index-1,nibbles)
            #return the answer
            return dynamic[index][nibbles]
        
        #return the value
        return candies(len(B)-1,D)
