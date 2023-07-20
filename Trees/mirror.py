'''
Given a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).
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
	# @return an integer
	def isSymmetric(self, A):

        #write a recursive function to get the comparison
        def compare(node_1,node_2):
            #the base case for the function
            if not node_1 and not node_2:
                return True
            elif not node_1 or not node_2:
                return False
            #compare the present values
            if node_1.val!=node_2.val:
                return False
            #else we would calculate for opposite sides
            return (
                compare(node_1.left,node_2.right)
                and
                compare(node_1.right,node_2.left)
            )

        #get the answer of the function
        answer=compare(A,A)

        #return the value
        return int(answer)
