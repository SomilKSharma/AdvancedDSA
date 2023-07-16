'''
Given a sorted array of integers A (0-indexed) of size N, find the left most and the right most index of a given integer B in the array A.

Return an array of size 2, such that 
          First element = Left most index of B in A
          Second element = Right most index of B in A.
If B is not found in A, return [-1, -1].

Note : Your algorithm's runtime complexity must be in the order of O(log n).
'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

        #get left/right variable
        left=right=-1

        #get the left most
        start=0
        end=len(A)-1

        while start<=end:
            #get the mid
            mid=(start+end)//2
            #check for equality
            if A[mid]==B:
                left=mid
                end=mid-1
            elif A[mid]<B:
                start=mid+1
            else:
                end=mid-1
        
        #get the right most
        start=0
        end=len(A)-1

        while start<=end:
            #get the mid
            mid=(start+end)//2
            #check for equality
            if A[mid]==B:
                right=mid
                start=mid+1
            elif A[mid]<B:
                start=mid+1
            else:
                end=mid-1
        
        #return the answer
        return left,right
        
