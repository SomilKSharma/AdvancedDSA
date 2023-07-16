#merge B and A as one sorted array
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):

        #create an answer array
        answer=[]

        #create two index
        index_a=index_b=0

        #iterate and fill the answer array
        while index_a<len(A) and index_b<len(B):
            #check which one is less
            if A[index_a]<B[index_b]:
                answer.append(A[index_a])
                index_a+=1
            else:
                answer.append(B[index_b])
                index_b+=1
        
        #while index of a is less than len(A)
        while index_a<len(A):
            answer.append(A[index_a])
            index_a+=1
        
        #while index of b is less than len(B)
        while index_b<len(B):
            answer.append(B[index_b])
            index_b+=1
    
        #return the answer
        return answer
        
