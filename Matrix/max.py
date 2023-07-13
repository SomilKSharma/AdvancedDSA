'''Given a matrix A of size NxM, which is row-wise and column-wise sorted. Find a submatrix such that sum of its elements is maximum and return this sum.'''
class Solution:
    # @param A : list of list of integers
     # @return an long
    def solve(self, A):

        #reverse row prefix sum
        for row in reversed(range(len(A)-1)):
            for col in range(len(A[0])):
                A[row][col]=A[row+1][col]+A[row][col]

        #reverse col prefix sum
        for row in range(len(A)):
            for col in reversed(range(len(A[0])-1)):
                A[row][col]=A[row][col+1]+A[row][col]
        
        #get the maximum value
        maxi=float('-inf')
        for row in range(len(A)):
            for col in range(len(A[0])):
                maxi=max(maxi,
                        A[row][col])
        
        return maxi

            
        
