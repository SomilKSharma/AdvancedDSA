'''
You are given a sorted array A of size N and a target value B. 
Your task is to find the index (0-based indexing) of the target value in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater than equal to B.
Your solution should have a time complexity of O(log(N)).
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):

        #edge case for B being greater than all values
        answer=len(A)

        #get the binary search
        start=0
        end=len(A)-1
        while start<=end:
            #get the mid
            mid=(start+end)//2
            #check for equality
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                start=mid+1
            else:
                answer=mid
                end=mid-1

        #return the answer
        return answer
