'''
Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.
In this case, return the length of the longest increasing subsequence.
'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):

        #create a dynamic array to get the answer
        dynamic=[
            -1
            for _ in range(len(A))
        ]

        #iterate for each value in the array and fill the dynamic array
        for index in range(len(A)):
            #compare the value and get the answer
            rev=index-1
            maxi=1
            while rev>-1:
                if A[rev]<A[index]:
                    maxi=max(maxi,dynamic[rev]+1)
                rev=rev-1
            #put the answer in the dynamic array
            dynamic[index]=maxi
        
        #return the max in the dynamic array
        return max(dynamic)
