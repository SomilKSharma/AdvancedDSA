'''Each query is of the form (l, r, c), where l and r are indices (1-based) representing a range in the array A, and c is an integer value.

For each query, you are required to add the value c to every element within the range [l, r] (inclusive).'''
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        #create an answer array
        answer=[0]*len(A)

        #fill the values in answer array
        for left,right,value in B:
            left,right=left-1,right-1
            answer[left]=answer[left]+value
            if right!=len(A)-1:
                answer[right+1]=answer[right+1]-value
        
        #do the prefix sum
        for index in range(1,len(answer)):
            answer[index]=answer[index-1]+answer[index]

        for index in range(len(A)):
            A[index]+=answer[index]
        
        return A
        
