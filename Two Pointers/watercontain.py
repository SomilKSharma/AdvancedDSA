'''
Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]).

N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''
class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArea(self, A):

        #create two pointers
        start,end=0,len(A)-1

        #get a maxi varible
        maxi=0

        #iterate till start<=end
        while start<=end:
            #get the minimum of the two
            mini=min(A[start],A[end])
            #check for maximum
            maxi=max(
                maxi,
                mini*(end-start)
            )
            #iterate to the next value
            if A[start]<A[end]:
                start+=1
            else:
                end-=1
        
        #return the answer
        return maxi

