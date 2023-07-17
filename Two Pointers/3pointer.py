'''
Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the sum of those three integers.
Assume that there will only be one solution.
'''
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):

        #sort the array
        A.sort()

        #get the three pointers
        first=second=third=0

        #get minimum difference
        mini=float('inf')
        answer=0

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
                if sums==B:
                    return B
                elif sums<B:
                    #store min sums difference
                    if mini>B-sums:
                        mini=B-sums
                        answer=sums
                    second=second+1
                else:
                    #store min sums difference
                    if mini>sums-B:
                        mini=sums-B
                        answer=sums
                    third=third-1
            #iterate first further
            first=first+1
            
        #return the mini difference
        return answer


