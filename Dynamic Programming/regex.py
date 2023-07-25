'''
Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' ? ' : Matches any single character.
' * ' : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):

        #get a dynamic array to store the value
        dynamic=[
            [-1]*len(B)
            for _ in range(len(A))
        ]

        #write a recurisve code to get the answer
        def regex(a,b):
            #base characters
            if a<0:
                #check if the remaining elements in B are '*'
                if B[:b+1].count('*')==(b+1):
                    return True
                return False
            elif b<0:
                return False
            #check if value in dynamic array
            if dynamic[a][b]!=-1:
                return dynamic[a][b]
            #else we would have to calculate the value
            else:
                #check if equal
                if A[a]==B[b] or B[b]=='?':
                    dynamic[a][b]=regex(a-1,b-1)
                elif B[b]=='*':
                    dynamic[a][b]=(
                        regex(a-1,b) or
                        regex(a,b-1)
                    )
                else:
                    dynamic[a][b]= False
            #return the answer
            return dynamic[a][b]
        
        #get the answer and return the int value
        return int(regex(len(A)-1,len(B)-1))
                
