'''
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.
'''

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):

        #function to store pallindrome dynamic
        pall=[
            [-1]*len(A)
            for _ in range(len(A))
        ]

        #function to check pallindrome
        def pallindrome(start,end):
            if start>end:
                return True
            if pall[start][end]!=-1:
                return pall[start][end]
            else:
                pall[start][end]=A[start]==A[end] and pallindrome(start+1,end-1)
            return pall[start][end]

        #store whether a given string(start/end) is pallindrome or not
        dynamic=[
            [-1]*len(A)
            for _ in range(len(A))
        ]

        #write a recursive function to get the Solution
        def partition(start,end):
            #base case
            if start==end:
                return 0
            #check if value in the dynamic array
            if dynamic[start][end]!=-1:
                return dynamic[start][end]
            else:
                if pallindrome(start,end):
                    dynamic[start][end]=0
                else:
                    #run a for loop for each index
                    mini=float('inf')
                    for index in range(start,end):
                        if pallindrome(start,index):
                            mini=min(
                                mini,
                                partition(start,index)+
                                partition(index+1,end)
                                +1
                            )
                    dynamic[start][end]=mini
            
            return dynamic[start][end]
        
        return partition(0,len(A)-1)
        
                    




