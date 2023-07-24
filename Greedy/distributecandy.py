'''
N children are standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum number of candies you must give?
'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def candy(self, A):

		#create a left array
		left=[1]*len(A)
		#create a right array
		right=[1]*len(A)

		#compare the present with the right
        for index in reversed(range(len(A)-1)):
            #compare the two and get the answer
            if A[index]>A[index+1]:
                left[index]=left[index+1]+1
		
        #compare the present with the left
        for index in range(1,len(A)):
            #compare the two and get the answer
            if A[index-1]<A[index]:
                right[index]=right[index-1]+1
        
        #get the answer
        answer=(
            max(left[index],right[index])
            for index in range(len(A))
        )

        #return the sum of the answer
        return sum(answer)
		

        
