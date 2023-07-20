'''
Given the root of a binary tree A. 
Return the sum of all the nodes of the binary tree.

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

        #write a function to get the sum
        def summation(node):
            #base case
            if not node:
                return 0
            #assume the code works for the left
            left=summation(node.left)
            #assume the code works for the right
            right=summation(node.right)
            #combine left and right with the present
            return node.val+left+right
        
        #get the answer into a variable
        sums=summation(A)

        #return the answer
        return sums
