#Are Matrices Same
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        rows,cols=len(A),len(A[0])

        for row in range(rows):
            for col in range(cols):
                if A[row][col]!=B[row][col]:
                    return 0
        else:
            return 1
