'''
Given a binary tree, return the 
preorder traversal of its nodes values.
'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

import sys
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):

        #get an array to store the answer
        preorder=[]

        #write a function to traverse in a preorder fashion
        def traversal_preorder(node):
            #base case of the function
            if not node:
                return
            #store the present value in the array
            preorder.append(node.val)
            #assume the code works for left and right nodes
            traversal_preorder(node.left)
            traversal_preorder(node.right)
        
        #call the function
        traversal_preorder(A)

        #return the value
        return preorder
