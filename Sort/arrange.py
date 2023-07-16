#Given an array A of non-negative integers, arrange them such that they form the largest number.
from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        
        #convert the tuple to an array
        A=list(map(str,A))

        #write a modified sorting function
        def sorting(s1,s2):
            #if case
            if s1+s2>=s2+s1:
                return -1
            else:
                return 1
        
        #sort using the modifed function
        A.sort(key=cmp_to_key(sorting))

        #return the array
        return int(''.join(A))
