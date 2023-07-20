'''
Given a binary tree, return the zigzag level order traversal of 
its nodes values. (ie, from left to right, then right to left for the next level and alternate between).
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
	def zigzagLevelOrder(self, A):

        #create two stacks for odd and even row
        odd=deque()
        even=deque()

        #add the first node to odd
        odd.append(A)

        #get an answer and a level array to store the answer and the level
        answer=[]
        level=[]

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
                    level.append(node.val)
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
                    level.append(node.val)
            #add the value of level to the answer
            answer.append(level)
        
        return answer


