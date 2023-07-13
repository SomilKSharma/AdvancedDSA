#Sub-matrix Sum Queries
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):

        #row wise prefix sum
        for row in range(1,len(A)):
            for col in range(len(A[0])):
                A[row][col]=A[row-1][col]+A[row][col]

        #col wise prefix sum
        for row in range(len(A)):
            for col in range(1,len(A[0])):
                A[row][col]=A[row][col-1]+A[row][col]
        
        #get an answer array
        answer=[]

        #iterate for each query
        for index in range(len(B)):
            #get the edges of the query matrix
            b,c,d,e=B[index]-1,C[index]-1,D[index]-1,E[index]-1
            #get sum till d,e
            sums=A[d][e]
            #remove extra cols
            if c:
                sums=sums-A[d][c-1]
            #remove extra rows
            if b:
                sums=sums-A[b-1][e]
            #add the needed but removed elements
            if b and c:
                sums=sums+A[b-1][c-1]
            #add to the answer
            answer.append(sums%1000000007)


        #return the value
        return answer

