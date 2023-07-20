'''
Given a binary search tree of integers. You are given a range B and C.
Return the count of the number of nodes that lie in the given range.
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
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        #get a global counter
        global counter
        counter=0

        #write the fucntion to calculate the value
        def bst_node_range(node):
            #global counter
            global counter
            #base case of the recursion
            if not node:
                return
            #check the present node
            if node.val<B:
                bst_node_range(node.right)
            elif node.val>C:
                bst_node_range(node.left)
            else:
                counter=counter+1
                bst_node_range(node.left)
                bst_node_range(node.right)
        
        #call the fucntion
        bst_node_range(A)

        #return the answer 
        return counter