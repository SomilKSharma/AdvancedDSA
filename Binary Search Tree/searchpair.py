'''
Given a binary search tree A, where each node contains a positive 
integer, and an integer B, you have to find whether or not there 
exist two different nodes X and Y such that X.value + Y.value = B.

Return 1 to denote that two such nodes exist. Return 0, otherwise.
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
	# @param B : integer
	# @return an integer
	def t2Sum(self, A, B):

        #create two stacks to store maximum and minimum
        maxi=deque()
        mini=deque()

        #create two pointers to point at nodes
        lefts=rights=A

        #iterate in a while loop indefinitely
        while True:

            #while the lefts pointer exists
            while lefts:
                mini.append(lefts)
                lefts=lefts.left
            
            #while the rights pointer exists
            while rights:
                maxi.append(rights)
                rights=rights.right
            
            #check whether the stacks have zero or same value
            if (
                (not maxi or not mini)
                or
                (maxi[-1]==mini[-1])
            ):
                #then the pair wasn't found
                return 0
            
            #else we would compare the values to get an answer
            sums=mini[-1].val+maxi[-1].val
            if sums==B:
                return 1
            #increment the minimum pointer
            elif sums<B:
                node=mini.pop()
                lefts=node.right
            #decrement to the maximum pointer
            else:
                node=maxi.pop()
                rights=node.left
        

            



