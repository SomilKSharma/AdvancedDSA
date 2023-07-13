#Given an array A of length N, return the subarray from B to C.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        #get an answer array
        answer=[]

        for index in range(len(A)):
            #check for the range
            if B<=index<=C:
                answer.append(A[index])
        
        #return the value
        return answer
