# Subarray with given sum and length
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        #edge case check
        if len(A)<B:
            return 0
        elif len(A)==B:
            return int(sum(A)==C)
        
        #get sum of the first B elements
        sums=sum(A[:B])

        #check for first sum
        if sums==C:
            return 1
        
        #else iterate using sliding window,comparing for each index
        for index in range(len(A)-B):
            #slide the sum
            sums=sums-A[index]+A[index+B]
            #compare with C
            if sums==C:
                return 1
        
        #else return 0
        return 0
