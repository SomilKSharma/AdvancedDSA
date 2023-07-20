'''
Given the root of a tree A with each node having a certain value, 
find the count of nodes with more value than all its ancestors.

Ancestor means that every node that occurs before the current 
node in the path from root to the node.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        #get a counter global variable
        global counter
        counter=0

        #write a function to get the value of nodes with value more than ancestor
        def count_maximums(node,ancestor_max):
            #declare global variable
            global counter
            #base case of the function
            if not node:
                return
            #check for this node
            if node.val>ancestor_max:
                counter+=1
                ancestor_max=node.val
            #assume the code works for left values
            count_maximums(node.left,ancestor_max)
            #assume the code works for right values
            count_maximums(node.right,ancestor_max)
        
        #call the function
        count_maximums(A,float('-inf'))

        #return the count
        return counter

            
