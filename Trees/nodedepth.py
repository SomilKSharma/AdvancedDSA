'''
Given a binary tree with root node pointer A . 
The depth of each node is the shortest distance to the root. 
A node is deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is that node, plus the set of all descendants
 of that node.

Return the node with the largest depth such that it contains all 
the deepest nodes of the entire tree lies in its subtree.

NOTE: All nodes values are uniques in the tree.
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
    # @return the root node in the tree
    def solve(self, A):

        #write function to get the node with all nodes of maximum depth
        def max_depth_node(node):
            #base case for the function
            if not node:
                return None,0
            #assume the code works for the left nodes
            answer_l,depth_l=max_depth_node(node.left)
            #assume the code works for the right nodes
            answer_r,depth_r=max_depth_node(node.right)
            #link the left and the right node with the present node
            #we have found our answer for present
            if depth_l==depth_r:
                return node,depth_l+1
            elif depth_l>depth_r:
                return answer_l,depth_l+1
            else:
                return answer_r,depth_r+1
        
        #get the answer node
        answer,_=max_depth_node(A)

        #return the answer node
        return answer
