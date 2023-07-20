'''
Two elements of a Binary Search Tree (BST), represented by root 
A are swapped by mistake. Tell us the 2 values, when swapped, 
will restore the Binary Search Tree (BST).
A solution using O(n) space is pretty straightforward. Could 
you devise a constant space solution?

Note: The 2 values must be returned in ascending order
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
	def recoverTree(self, A):

        #global variables
        global left,right,previous
        #create the two values
        left=right=0
        #create a previous value
        previous=0

        #iterate in a preorder fashion to compare consecutive nodes
        def inorder(node):
            #global variables 
            global left,right,previous
            #base case
            if not node:
                return
            #call the left of the tree
            inorder(node.left)
            #compare the present value with the previous value
            if previous and not left:
                #compare the values
                if previous>node.val:
                    left,right=previous,node.val
            elif previous and left:
                #compare the values
                if previous>node.val:
                    right=node.val
            #store the previous value
            previous=node.val
            #call the right of the tree
            inorder(node.right)
        
        #call the function
        inorder(A)
        #return the value
        return right,left

