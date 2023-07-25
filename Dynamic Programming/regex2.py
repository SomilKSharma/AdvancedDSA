'''
Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' . ' : Matches any single character.
' * ' : Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):

        #create a dynamic array
        dynamic=[
            [-1]*len(B)
            for _ in range(len(A))
        ]

        #write a recursive function to get the answer
        def regex(a,b):
            #base case of the function
            if a<0 and b<0:
                return True
            elif a<0:
                #check of the "*"
                if B[b]=='*':
                    return True
                else:
                    return False
            elif b<0:
                return False
            #check for value in the dynamic array
            if dynamic[a][b]!=-1:
                return dynamic[a][b]
            #else we would calculate the value
            else:
                #check for equality
                if A[a]==B[b] or B[b]=='.':
                    dynamic[a][b]=regex(a-1,b-1)
                elif B[b]=='*' and (B[b-1]==A[a] or B[b-1]=='.'):
                    dynamic[a][b]=(
                        regex(a,b-2) or
                        regex(a-1,b)
                    )
                elif B[b]=='*' and B[b-1]!=A[a]:
                    dynamic[a][b]=regex(a,b-2)
                else:
                    dynamic[a][b]=False
            #return the value
            return dynamic[a][b]
        
        #return the answer
        return int(regex(len(A)-1,len(B)-1))