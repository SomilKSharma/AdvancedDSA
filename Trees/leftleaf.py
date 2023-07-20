'''
Given a binary tree, find and return the sum of node value 
of all left leaves in it.
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

        #write a function to get the sum of left leaves
        def left_leaf_sum(node,is_left):
            #base case
            if not node:
                return 0
            #assume the code works for left end of the tree
            sum_1=left_leaf_sum(node.left,True)
            #assume the code works for right end of the tree
            sum_2=left_leaf_sum(node.right,False)
            #check the present node
            if not node.left and not node.right and is_left:
                return node.val+sum_1+sum_2
            else:
                return sum_1+sum_2
        
        #call the function and get the answer
        answer=left_leaf_sum(A,False)

        #return the answer
        return answer

