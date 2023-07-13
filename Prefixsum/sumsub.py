#Sum of All Subarrays
class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):

        #get a sums variable
        total_sum=0

        for index,value in enumerate(A):
            total_sum=total_sum+(
                value*(index+1)*(len(A)-index)
            )
        
        return total_sum
