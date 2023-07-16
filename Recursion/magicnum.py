class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #use the divisibility rule of 9
        if A%9==1:
            return 1
        else:
            return 0
