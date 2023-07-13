#Equilibrium index
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #left prefix sum
        left=A.copy()
        for index in range(1,len(A)):
            left[index]=left[index-1]+left[index]
        
        #right prefix sum
        right=A.copy()
        for index in reversed(range(len(A)-1)):
            right[index]=right[index]+right[index+1]
        
        #check for 0 index
        if right[1]==0:
            return 0

        #check for middle elements
        for index in range(1,len(A)-1):
            #check for left and right indices
            if left[index-1]==right[index+1]:
                return index
        
        #check for last index
        if left[-2]==0:
            return len(A)-1
        
        #else not found, return -1
        return -1
