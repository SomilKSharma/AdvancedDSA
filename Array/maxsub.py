#Maximum subarray sum of fixed length
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B):

        #edge case check
        if len(A)<B:
            return 0
        elif len(A)==B:
            return sum(A)
        
        #get sum of the first B elements
        sums=sum(A[:B])

        #make it the maximum
        maxi=sums
        
        #else iterate using sliding window,comparing for each index
        for index in range(len(A)-B):
            #slide the sum
            sums=sums-A[index]+A[index+B]
            #compare with C
            maxi=max(maxi,sums)
        
        #else return 0
        return maxi
