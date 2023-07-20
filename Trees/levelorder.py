'''
Given a binary tree, return the level order traversal of its 
nodes' values. (i.e., from left to right, level by level).
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import sys
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):

        #create a queue for level order traversal
        queue=deque()

        #get an answer array for the solution
        answer=[]
        #get a level array to store value of each level
        level=[]

        #put the first node in queue
        queue.append(A)

        #iterate till the queue is not empty
        while queue:
            #initialise level array again
            level=[]
            #iterate for all the node of one level
            for _ in range(len(queue)):
                #get the node
                node=queue.popleft()
                #check if node has a left or a right and then add them
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                #add value to the level array
                level.append(node.val)
            #add all the elements of this level to the array
            answer.append(level)
        
        #return the answer array
        return answer


