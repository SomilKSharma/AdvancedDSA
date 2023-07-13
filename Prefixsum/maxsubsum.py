#Maximum subarray sum
class Solution:
    # @param A : list of integers
     # @return an long
    def solve(self, A):

        #get an answer array
        answer=[]

        #get a maxi dummy variable
        maxi=float('-inf')

        for index_1 in range(len(A)):
            sums=0
            for index_2 in range(index_1,len(A)):
                sums=sums+A[index_2]
                maxi=max(maxi,sums)
        
        return maxi