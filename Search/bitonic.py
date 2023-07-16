'''
Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get a peak variable
        peak=0

        #get the edge cases of first and last being peak
        if A[0]>A[1]:
            peak=0
        elif A[-1]>A[-2]:
            peak=len(A)-1
        else:
            #else binary search in 1 to len(A)-2 search space
            start,end=1,len(A)-2
            while start<=end:
                #get the mid value
                mid=(start+end)//2
                #compare for peak
                if A[mid-1]<A[mid]>A[mid+1]:
                    peak=mid
                    break
                elif A[mid-1]>A[mid]>A[mid+1]:
                    end=mid-1
                else:
                    start=mid+1
        
        #search to the left of peak
        start=0
        end=peak
        while start<=end:
            #get the mid
            mid=(start+end)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                start=mid+1
            else:
                end=mid-1
        
        #search to the right of peak
        start=peak+1
        end=len(A)-1
        while start<=end:
            #get the mid
            mid=(start+end)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                end=mid-1
            else:
                start=mid+1
        
        #return -1 if none exists
        return -1
        
                
