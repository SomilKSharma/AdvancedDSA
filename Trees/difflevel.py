'''
Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level.
NOTE: Consider the level of root node as 1.
'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from collections import deque
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def solve(self, A):

        #create two stacks for odd and even row
        odd=deque()
        even=deque()

        #add the first node to odd
        odd.append(A)

        #get a sums variable
        sums=0

        #iterate till there is something in the stack
        while odd or even:
            #re-initialise level
            level=[]
            #iterate for each value in the present stack
            if odd:
                #iterate for odd stack
                for _ in range(len(odd)):
                    #get the node
                    node=odd.pop()
                    #add values to the stack
                    if node.left:
                        even.append(node.left)
                    if node.right:
                        even.append(node.right)
                    #add value to the level
                    sums=sums+node.val
            else:
                #iterate for even stack
                for _ in range(len(even)):
                    #get the node
                    node=even.pop()
                    #add values to the stack
                    if node.right:
                        odd.append(node.right)
                    if node.left:
                        odd.append(node.left)
                    #add value to the level
                    sums=sums-node.val

        #return the sums value
        return sums


