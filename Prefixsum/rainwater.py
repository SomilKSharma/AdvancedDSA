#Rain Water Trapped
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):

        #get a prefix maximum array
        prefix=[
            0
            for _ in range(len(A))
        ]
        maxi=float('-inf')

        #iterate for other values in the array
        for index,value in enumerate(A):
            #get the maximum value upto the index
            if value>maxi:
                maxi=value
            #add the value to prefix maximum
            prefix[index]=maxi
        
        #get a suffix maximum
        suffix=[
            0
            for _ in range(len(A))
        ]
        maxi=float('-inf')

        #iterate for all values if A in reversed order
        for index in reversed(range(len(A))):
            #check for maximum upto the index
            if A[index]>maxi:
                maxi=A[index]
            #add value to the suffix array
            suffix[index]=maxi
        
        #water storing variable
        water=0
        for index in range(1,len(A)-1):
            #get minimum of maximums at the index
            mini=min(prefix[index],suffix[index])
            if mini>A[index]:
                water=water+(
                    mini-A[index]
                )
        
        #return the answer
        return water
