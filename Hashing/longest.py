#Find the length of the longest set of consecutive elements from array A.
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):

        #convet the tuple to an array
        A=list(set(A))

        #sort the array
        A.sort()

        #get a maxi and a present length
        maxi=length=1

        #iterate for each index
        for index in range(1,len(A)):
            #check for next element
            if A[index]==A[index-1]+1:
                length=length+1
                maxi=max(maxi,length)
            #else case
            else:
                length=1
        
        #return the maximum
        return maxi
