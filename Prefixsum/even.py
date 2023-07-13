#Sum of even indices
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        #even index sum
        even=[
            0
            for _ in range(len(A))
        ]
        even[0]=A[0]
        for index in range(1,len(A)):
            #add element for even index
            add=A[index] if not index&1 else 0
            #put the value in prefix sum array
            even[index]=even[index-1]+add
        
        #get the answer array
        answer=[]

        #loop for all values of B
        for start,end in B:
            #check if start is at 0
            answer.append(even[end] if not start
                            else
                            even[end]-even[start-1]
            )
        
        #return the answer
        return answer
