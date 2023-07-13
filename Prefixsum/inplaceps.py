# In-place Prefix Sum
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]
        
        return A
