'''Given an array of integers A, find and return the peak element in it. 
An array element is considered a peak if it is not smaller than its neighbors. For corner elements, we need to consider only one neighbor. 

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #edge case if len(A)==1
        if len(A)==1:
            return A[0]
        
        #edge case of first and last being peak
        if A[0]>A[1]:
            return A[0]
        elif A[-1]>A[-2]:
            return A[-1]
        
        #binary search to look for other peak
        start,end=1,len(A)-2
        while start<=end:
            #get the mid
            mid=(start+end)//2
            #check for peak
            if A[mid-1]<=A[mid]>=A[mid+1]:
                return A[mid]
            elif A[mid-1]<A[mid]<A[mid+1]:
                start=mid+1
            else:
                end=mid-1
        
        #return -1 if no peak
        return -1
