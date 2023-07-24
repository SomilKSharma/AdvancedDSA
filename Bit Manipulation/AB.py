#Set the A-th bit and B-th bit in 0, and return output in decimal Number System.
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #return by left shifting and doing or
        return (1<<A)| (1<<B)
        
        
