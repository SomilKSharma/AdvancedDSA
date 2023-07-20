'''
Given a binary tree, return the Postorder traversal of its 
nodes values.
'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

import sys
sys.setrecursionlimit(10**9)
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):

        #get an array to store the value of the traversal
        postorder=[]

        #write a function to iterate in a postorder fashion
        def traversal_postorder(node):
            #write the base case of the code
            if not node:
                return
            #assume the code works for left node
            traversal_postorder(node.left)
            #assume the code works for right node
            traversal_postorder(node.right)
            #connect left and right with the node
            postorder.append(node.val)
        
        #call the function
        traversal_postorder(A)

        #return the value
        return postorder

