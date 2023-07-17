'''
Given an array A of N integers, are there elements a, b, c in S such that a + b + c = 0
Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c) The solution set must not contain duplicate triplets.
'''
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def threeSum(self, A):

        #list
        A=list(A)
        A.sort()

        #get the three pointers
        first=second=third=0

        #get answer
        answer=set()

        #iterate for all the pointers
        while first<len(A):
            #get the second and the third pointers
            second=first+1
            third=len(A)-1
            #iterate
            while second<third:
                #get the sum out of the three
                sums=A[first]+A[second]+A[third]
                #check for equality
                if sums==0:
                    answer.add((A[first],A[second],A[third]))
                    third=third-1
                elif sums<0:
                    second=second+1
                else:
                    third=third-1
            #iterate first further
            first=first+1
            
        #return the mini difference
        return list(answer)



