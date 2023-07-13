#For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        #get an even count array
        even=[
            0
            for _ in range(len(A))
        ]
        even[0]=0 if A[0]&1 else 1

        #fill values for all index of even
        for index in range(1,len(even)):
            #check if A[index] is even or not
            add=0 if A[index]&1 else 1
            even[index]=even[index-1]+add

        #get an answer array
        answer=[]

        #iterate over all the queries of B
        for start,end in B:
             #add the answer after checking for start index
             answer.append(even[end] if not start
                            else
                            even[end]-even[start-1])
        
        #return the answer
        return answer
