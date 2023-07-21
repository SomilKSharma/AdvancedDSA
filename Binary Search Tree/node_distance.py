'''
Given a binary search tree.
Return the distance between two nodes with given two keys B and C. 
It may be assumed that both keys exist in BST.

NOTE: Distance between two nodes is number of edges between them.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        #write a function to find the first element in range of B and C
        def bst_lca(node):
            #check for the condition
            if min(B,C)<=node.val<=max(B,C):
                return node
            #else iterate to the either sides
            elif node.val<=min(B,C):
                return bst_lca(node.right)
            else:
                return bst_lca(node.left)
        
        #get the lca node
        lca=bst_lca(A)

        #find distance of a node from lca
        def distance(node,value):
            #base case
            if not node:
                return False,0
            #check for the left side
            found_left,distance_left=distance(node.left,value)
            #check for the right side
            found_right,distance_right=distance(node.right,value)
            #check for found
            if node.val==value:
                return True,0
            elif found_left:
                return True,distance_left+1
            elif found_right:
                return True,distance_right+1
            else:
                return False,0
        
        #get the distance between lca and B
        _,b_distance=distance(lca,B)
        #get the distance between lca and C
        _,c_distance=distance(lca,C)

        #return the distance
        return b_distance+c_distance

