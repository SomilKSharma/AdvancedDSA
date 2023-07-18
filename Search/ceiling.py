'''
Given a sorted array B of integers of size A, 
and a integer value C, return the ceiling of C which is present 
in array B.
'''
class Solution:
    # @param A : integer\
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        #edge case if C is greater than all values of B
        answer=-1

        #binary search to get the ceiling
        start,end=0,len(B)-1
        while start<=end:
            #get the mid value 
            mid=(start+end)//2
            #check if equal
            if B[mid]==C:
                return C
            elif B[mid]<C:
                start=mid+1
            else:
                answer=B[mid]
                end=mid-1
        
        #return the answer
        return answer