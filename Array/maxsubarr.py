#maximum sum of contiguous non-empty subarray
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):

        #get the maximum sum variable
        maxi=float('-inf')

        #get a sums variable
        sums=0

        #iterate for all values in the array
        for value in A:
            #sum up
            sums=sums+value
            #compare with maximum
            maxi=max(maxi,sums)
            #check if sum is negative
            if sums<0:
                sums=0
        
        #return the maximum
        return maxi
