#maximum value in subarray from i to N-1.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #get a suffix maximum
        suffix=[
            0
            for _ in range(len(A))
        ]
        maxi=float('-inf')

        #iterate for all values if A in reversed order
        for index in reversed(range(len(A))):
            #check for maximum upto the index
            if A[index]>maxi:
                maxi=A[index]
            #add value to the suffix array
            suffix[index]=maxi
        
        #return the matrix
        return suffix
