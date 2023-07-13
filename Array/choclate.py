'''There are B number of students, the task is to distribute chocolate packets following below conditions:

1. Each student gets one packets.
2. The difference between the number of chocolates given to any two students is minimum.'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #base case
        if not B or len(A)<B:
            return 0
        
        #else sort the array
        A.sort()

        #get a mini variable
        mini=max(A)

        #iterate for difference of B in the sorted array
        for index in range(len(A)-B+1):
            mini=min(
                mini,
                A[index+B-1]-A[index]
            )
        
        return mini

