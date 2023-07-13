#Return a 2D array consisting of all the subarrays of the array
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):

        #get an answer array
        answer=[]

        #iterate for all values of A
        for index_1 in range(len(A)):
            for index_2 in range(index_1,len(A)):
                answer.append(
                    A[index_1:index_2+1]
                )
        
        #return
        return answer
