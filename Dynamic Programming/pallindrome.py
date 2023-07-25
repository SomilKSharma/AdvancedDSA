'''
Given a string A. Find the longest palindromic subsequence (A subsequence which does not need to be contiguous and is a palindrome).
You need to return the length of longest palindromic subsequence.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        #reverse the string to get a new string
        B=A[::-1]

        #create a dynamic array to store the answer
        dynamic=[
            [-1]*len(B)
            for _ in range(len(A))
        ]

        #create a recursive function to get the answer
        def lcs(a,b):
            #base case of the recursive code
            if a<0 or b<0:
                return 0
            #check if value in the dynamic array
            if dynamic[a][b]!=-1:
                return dynamic[a][b]
            #else we would have to calculate the value
            else:
                #get the value
                if A[a]==B[b]:
                    dynamic[a][b]=lcs(a-1,b-1)+1
                else:
                    dynamic[a][b]=max(
                        lcs(a-1,b),
                        lcs(a,b-1)
                    )
                #return the calculated value
                return dynamic[a][b]
        
        #return the answer
        return lcs(len(A)-1,len(B)-1)

