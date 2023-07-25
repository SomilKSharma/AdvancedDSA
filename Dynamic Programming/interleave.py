'''
Given A, B, C find whether C is formed by the interleaving of A and B.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : string
	# @param B : string
	# @param C : string
	# @return an integer
	def isInterleave(self, A, B, C):

        #edge case of difference in the length
        if len(C)!=len(A)+len(B):
            return 0

        #get a dynamic array to get the answer
        dynamic=[
            [-1]*len(B)
            for _ in range(len(A))
        ]

        #write a function to get the answer
        def interleaving(a,b):
            #check for the base case
            if a<0 and b<0:
                return True
            elif a<0:
                return B[:b+1]==C[:b+1]
            elif b<0:
                return A[:a+1]==C[:a+1]
            #else check the value in the dynamic array
            if dynamic[a][b]!=-1:
                return dynamic[a][b]
            #else we would calculate the value
            else:
                #check for equality
                if A[a]==C[a+b+1] and B[b]==C[a+b+1]:
                    dynamic[a][b]=(
                        interleaving(a-1,b) or
                        interleaving(a,b-1)
                    )
                elif A[a]==C[a+b+1]:
                    dynamic[a][b]=interleaving(a-1,b)
                elif B[b]==C[a+b+1]:
                    dynamic[a][b]=interleaving(a,b-1)
                else:
                    return False
            #return the answer
            return dynamic[a][b]
        
        #get the answer
        return int(interleaving(len(A)-1,len(B)-1))
