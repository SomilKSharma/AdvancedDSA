#Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #by using simple algebra, the maximum would be abs(A-B)%M=0
        return max(A,B)-min(A,B)

