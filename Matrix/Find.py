'''Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.'''

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #start from the top right corner
        row=0
        col=len(A[0])-1

        #get the answer variable
        answer=float('inf')

        #iterate for each value of A
        while row<len(A) and col>=0:
            #get the value at the present index
            value=A[row][col]
            #if equal
            if value==B:
                #calculate value
                dummy=(row+1)*1009+(col+1)
                answer=min(answer,dummy)
                col=col-1
            elif value<B:
                row=row+1
            else:
                col=col-1
        
        #return the answer
        if answer==float('inf'):
            return -1
        else:
            return answer


