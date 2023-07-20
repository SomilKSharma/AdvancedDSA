'''
Given preorder and inorder traversal of a tree, 
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

        #write a recursive code to get the answer
        def tree_construction(preorder,inorder):
            #base case of the function
            if not preorder or not inorder:
                return
            #get the node value
            node_value=preorder[0]
            #get the index of the node in inorder
            node_index=inorder.index(node_value)
            #create the node
            node=TreeNode(node_value)
            #provide left and right values to the node
            node.left=tree_construction(
                preorder[1:1+node_index],
                inorder[:node_index]
            )
            node.right=tree_construction(
                preorder[1+node_index:],
                inorder[node_index+1:]
            )
            #return the node
            return node
        
        #get the tree head
        root=tree_construction(A,B)

        #return the reference of root
        return root
