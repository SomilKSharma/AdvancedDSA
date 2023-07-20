'''
Given a binary tree A, invert the binary tree and return it.
Inverting refers to making the left child the right child and 
vice versa.
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
	# @return the root node in the tree
	def invertTree(self, A):

        #iterate for each node in the Tree
        def inversion(node):
            #check for the base case
            if not node:
                return
            #assume the code works for all nodes to the left
            inversion(node.left)
            #assume the code works for all nodes to the right
            inversion(node.right)
            #link left and the right with the present node
            node.left,node.right=node.right,node.left
        
        #call the function
        inversion(A)

        #return the inverted tree
        return A

