#Find and return the maximum possible sum of the B elements that were removed after the B operations.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get the length of the remaining elements
        least=len(A)-B

        #get the minimum sum of 'least' elements
        mini=sums=sum(A[:least])

        #sliding window for the Solution
        for index in range(len(A)-least):
            sums=sums-A[index]+A[index+least]
            mini=min(mini,sums)
        
        #reduce mini from the toal sum to get the maximum
        return sum(A)-mini
