# Find the row with the maximum number of 1.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        #get the variables needed
        row=0
        col=len(A[0])-1
        answer=0

        #iterate for each row
        while row<len(A):
            #iterate for each col to find the maximum 1
            while col>-1 and A[row][col]==1:
                answer=row
                col=col-1
            #increment the row
            row=row+1
        
        #return the answer
        return answer
