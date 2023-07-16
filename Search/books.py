'''
Given an array of integers A of size N and an integer B.

The College library has N books. The ith book has A[i] number of pages.

You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.
'''
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):

        if B>len(A):
            return -1

        def checker(pages):
            count=1
            sums=A[0]

            for value in A[1:]:
                sums=sums+value
                if sums>pages:
                    sums=value
                    count+=1
            
            return count<=B
        
        start=max(A)
        end=sum(A)
        answer=0
        while start<=end:
            mid=(start+end)//2
            if checker(mid):
                answer=mid
                end=mid-1
            else:
                start=mid+1
                
        
        return answer

