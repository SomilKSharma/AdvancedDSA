#Return 1 if B-th bit in A is set
#Return 0 if B-th bit in A is unset
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #return the value
        return (A>>B)&1
