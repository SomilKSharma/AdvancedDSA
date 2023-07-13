#add
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        rows,cols=len(A),len(A[0])

        return [[A[row][col]+B[row][col]
                for col in range(cols)]
                for row in range(rows)]