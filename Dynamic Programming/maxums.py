'''
You are given an array A of N integers and three integers B, C, and D.

You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        #create a dynamic array
        dynamic=[
            [0]*len(A)
            for _ in range(3)
        ]

        #iterate for the first row(A[i]*B)
        dynamic[0][0]=A[0]*B
        for index in range(1,len(A)):
            #get the maximum upto an index
            dynamic[0][index]=max(
                dynamic[0][index-1],
                A[index]*B
            )
        
        #iterate for the second row(A[j]*C)
        dynamic[1][0]=dynamic[0][0]+A[0]*C
        for index in range(1,len(A)):
            #get the maximum upto the index
            dynamic[1][index]=max(
                dynamic[1][index-1],
                dynamic[0][index]+A[index]*C
            )
        
        #iterate for the third row(A[k]*D)
        dynamic[2][0]=dynamic[1][0]+A[0]*D
        for index in range(1,len(A)):
            #get the maximum upto the index
            dynamic[2][index]=max(
                dynamic[2][index-1],
                dynamic[1][index]+A[index]*D
            )
        
        #return the maximum possible value
        return dynamic[2][len(A)-1]