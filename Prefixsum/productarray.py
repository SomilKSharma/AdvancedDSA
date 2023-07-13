'''find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #left products
        left=A.copy()
        for index in range(1,len(left)):
            left[index]=left[index-1]*left[index]
        
        #right products
        right=A.copy()
        for index in reversed(range(len(right)-1)):
            right[index]=right[index+1]*right[index]
        
        #get the answer array
        answer=[
            0
            for _ in range(len(A))
        ]
        answer[0]=right[1]
        answer[-1]=left[-2]

        #iterate for all other values
        for index in range(1,len(answer)-1):
            answer[index]=left[index-1]*right[index+1]
        
        return answer
