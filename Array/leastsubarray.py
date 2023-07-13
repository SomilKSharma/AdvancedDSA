# find the subarray of size K with the least average.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get the sum of first window of length B
        sums=0
        for index in range(B):
            sums+=A[index]
        
        mini=sums 
        answer=0

       #slide the window
        for index in range(len(A)-B):
            sums=sums-A[index]+A[index+B]
            if mini>sums:
                mini=sums
                answer=index+1
        
        return answer
        
