'''
Given two binary trees, check if they are equal or not.
Two binary trees are considered equal if they are structurally 
identical and the nodes have the same value.
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
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):

        #write a recursive code to get the comparison
        def compare(node_a,node_b):
            #base case of the function
            if not node_a and not node_b:
                return True
            elif not node_a or not node_b:
                return False
            #compare the two values
            if node_a.val!=node_b.val:
                return False
            #else compare for other values assuming the function would work
            return True and compare(node_a.left,node_b.left) and compare(node_a.right,node_b.right)

        #get the answer to the values
        answer=compare(A,B)

        #return the int format of the answer
        return int(answer)