'''
Given an array of integers A and an integer B, find and 
return the maximum value K such that there is no subarray 
in A of size K with the sum of elements greater than B.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        #length
        length=len(A)

        #checker function
        def checker(mid):
            sums=maxi=sum(A[:mid])
            for index in range(length-mid):
                sums=sums-A[index]+A[index+mid]
                maxi=max(sums,maxi)
            
            return maxi<=B

        #binary search
        answer=0
        start,end=1,length
        while start<=end:
            mid=(start+end)//2
            if checker(mid):
                answer=mid
                start=mid+1
            else:
                end=mid-1
        
        return answer

