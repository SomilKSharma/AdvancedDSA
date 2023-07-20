'''
You are given a binary tree represented by root A. You need to check 
if it is a Binary Search Tree or not.
'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):

        #write a recursive function to get the answer
        def check_validity(start,node,end):
            #base case of the recursive function
            if not node:
                return True
            #check for the present
            if start>=node.val or node.val>=end:
                return False
            #else the answer would depend on left and the right
            else:
                return (
                    check_validity(start,node.left,node.val)
                    and
                    check_validity(node.val,node.right,end)
                )

        #call the function the store the answer
        answer=check_validity(float('-inf'),A,float('inf'))

        #return the answer in integer
        return int(answer)