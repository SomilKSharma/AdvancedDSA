#Sum of odd indices
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        #even indices
        even=[0]*len(A)
        even[0]=0
        for index in range(1,len(A)):
            add=A[index] if index&1 else 0
            even[index]=even[index-1]+add
        
        #answer
        answer=[]

        #iterat through the queries
        for left,right in B:
            if not left:
                answer.append(even[right])
            else:
                answer.append(even[right]-even[left-1])

        return answer      