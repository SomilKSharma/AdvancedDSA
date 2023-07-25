'''
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):

        #create a dynamic array to get the answer
        dynamic=[
            [-1]*len(B)
            for _ in range(len(A))
        ]

        #write a recursive code to get the answer
        def steps_convert(a,b):
            #base case
            if a<0:
                return b+1
            elif b<0:
                return a+1
            #check for the dynamic array for the answer
            if dynamic[a][b]!=-1:
                return dynamic[a][b]
            #else we would calculate the value
            else:
                #check if equal
                if A[a]==B[b]:    
                    dynamic[a][b]=steps_convert(a-1,b-1)
                else:
                    dynamic[a][b]=min(
                        steps_convert(a-1,b-1),
                        steps_convert(a-1,b),
                        steps_convert(a,b-1)
                    )+1
            #return the value
            return dynamic[a][b]
        
        #return the answer to the array
        return steps_convert(len(A)-1,len(B)-1)
