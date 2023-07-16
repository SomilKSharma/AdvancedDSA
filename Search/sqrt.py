'''
Given an integer A. Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).

The value of A can cross the range of Integer.

NOTE: 
   Do not use the sqrt function from the standard library. 
   Users are expected to solve this in O(log(A)) time.
'''
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):

        #set the search space
        start=0
        end=A

        #binary search
        answer=0
        while start<=end:
            #get the middle element
            mid=(start+end)//2
            #check if element found
            if mid*mid==A:
                answer=mid
                break
            elif mid*mid<A:
                answer=mid
                start=mid+1
            else:
                end=mid-1
        
        #return the answer
        return answer
