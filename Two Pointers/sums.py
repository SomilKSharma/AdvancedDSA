'''
Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get the start and end pointer
        start,end=0,len(A)-1

        #get a counter
        counter=0

        #get a left and a right freq
        left=right=0

        #iterate till start<=end:
        while start<=end:
            #get the sum of the value
            sums=A[start]+A[end]
            #check if less
            if sums<B:
                start=start+1
            #if more iterate further
            elif sums>B:
                end=end-1
            else:
                #if equal calculate frequency
                #check for equality
                if A[start]==A[end]:
                    counter=counter+(end-start)*(end-start+1)//2
                    break
                #get the number of left frequency
                left=1
                start=start+1
                while A[start]==A[start-1]:
                    left=left+1
                    start=start+1
                #get the number of right frequency
                right=1
                end=end-1
                while A[end]==A[end+1]:
                    right=right+1
                    end=end-1
                #add to the counter
                counter=counter+left*right
            
        #return counter
        return counter%1000000007
                
            
