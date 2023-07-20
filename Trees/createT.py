'''
Given the inorder and postorder traversal of a tree, 
construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.
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
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):

        #write a function to construct a tree out of the values we have
        def construction(inorder,postorder):
            #base case
            if not inorder or not postorder:
                return 
            #get the node value
            node_value=postorder[-1]
            #get index of the node value in inorder
            node_index=inorder.index(node_value)
            #create the node
            node=TreeNode(node_value)
            #link node to the left and the right values
            node.left=construction(
                inorder[:node_index],
                postorder[:node_index]
            )
            node.right=construction(
                inorder[node_index+1:],
                postorder[node_index:-1]
            )
            #return the node value
            return node
        
        #store the node value in the root variable and return
        root=construction(A,B)
        #return the answer
        return root