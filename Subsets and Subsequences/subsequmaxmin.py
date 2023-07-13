#for each subsequence, find the difference between the largest and smallest number in that subsequence.
class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):

        #sort the array
        A.sort()

        #get a sums variable
        sums=0
        #iterate for each value of the array
        for index in range(len(A)):
            #get the sum according to value in the sorted array
            sums=sums+(
                A[index]*(2**(index))-A[index]*(2**(len(A)-index-1))
            )
        
        #return the value
        return sums
