#For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):

        #get the prefix sum of the array
        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]
        
        answer=[]
        for left,right in B:
            if not left:
                answer.append(A[right])
            else:
                answer.append(A[right]-A[left-1])
        
        return answer
