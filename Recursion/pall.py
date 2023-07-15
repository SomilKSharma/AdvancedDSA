#pallindrome check using recursion
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        #recursive function
        def pallindrome(start,end):
            #base case
            if start>end:
                return True
            #check for interior string
            value=pallindrome(start+1,end-1)
            #connect interior witht the present
            return value and A[start]==A[end]
        
        return int(pallindrome(0,len(A)-1))
