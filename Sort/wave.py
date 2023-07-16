#In other words, arrange the elements into a sequence such that
#a1 >= a2 <= a3 >= a4 <= a5..... 

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):

        #sort the array
        A.sort()

        #iterate for all even index and replace alternate
        for index in range(0,len(A)-1,2):
            A[index],A[index+1]=A[index+1],A[index]
        
        #return the value
        return A
