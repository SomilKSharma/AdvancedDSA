#For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        #create the prefix sum of A
        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]
        
        #get ana answer array
        answer=[]

        #iterate for B values
        for start,end in B:
            #add the sum to the answer
            answer.append(A[end] if not start else
                            A[end]-A[start-1])
        
        #return the answer
        return answer
