#Reverse the Array
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):

        #get another array
        answer=[]

        #iterate reverse in the A array
        for value in reversed(A):
            answer.append(value)

        #return the value
        return answer