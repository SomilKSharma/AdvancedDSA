'''
You are given three positive integers, A, B, and C.

Any positive integer is magical if divisible by either B or C.

Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

Note: Ensure to prevent integer overflow while calculating.
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        #write a function to get the hcf
        def hcf(B,C):
            #base case
            if not C:
                return B
            #else recall thr function
            return hcf(C,B%C)
        
        #get the lcm
        lcm=(C*B)//hcf(B,C)

        #write the binary search
        answer=0
        start,end=0,min(B,C)*A
        while start<=end:
            #get the middle
            mid=(start+end)//2
            #get the magical number upto mid
            magic=mid//B+mid//C-mid//lcm
            #check
            if magic==A:
                answer=mid
                end=mid-1
            elif magic>A:
                end=mid-1
            else:
                start=mid+1
        
        #return the answer
        return answer%1000000007

