'''
Given preorder traversal of a binary tree, check if it is 
possible that it is also a preorder traversal of a Binary Search 
Tree (BST), where each internal node (non-leaf nodes) have exactly 
one child.
'''

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):

        #get an answer variable
        answer='YES'

        #get the maximum and minimum
        maximum=max(A[-1],A[-2])
        minimum=min(A[-1],A[-2])

        #iterate for each value in the array in a reverse fashion
        for value in A[::-1][2:]:
            #check the value
            if minimum<=value<=maximum:
                answer='NO'
                break
            #else update the value
            maximum=max(maximum,value)
            minimum=min(minimum,value)
        
        #return the answer
        return answer
