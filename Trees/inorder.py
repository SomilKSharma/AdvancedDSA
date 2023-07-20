'''
Given a binary tree, return the inorder traversal 
of its nodes' values.
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
	def inorderTraversal(self, A):

        #get an inorder array to store the answer
        inorder=[]

        #write a function iterate in an inorder fashion
        def inorder_traversal(node):
            #base case of the function
            if not node:
                return 
            #assume the code works for the left and iterate to it
            inorder_traversal(node.left)
            #store the present values
            inorder.append(node.val)
            #assume the code works for the right and iterate to it
            inorder_traversal(node.right)
        
        #call the function
        inorder_traversal(A)

        #return the value of the function
        return inorder
