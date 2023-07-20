'''
You are given the root node of a binary tree A. 
You have to find the max value of all node values of this tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        #global maximum
        global maximum
        maximum=float('-inf')

        #write a recursive code to find the maximum value
        def inorder(node):
            #global maximum
            global maximum
            #base case for the recursive code
            if not node:
                return
            #assume the code works for the left side
            inorder(node.left)
            #check the present
            maximum=max(
                maximum,
                node.val
            )
            #assume the code works on the right side
            inorder(node.right)
        
        #call the function
        inorder(A)

        #return the maximum
        return maximum
            

