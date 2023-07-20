'''
You are given the root node of a binary tree A. 
You have to find the height of the given tree.

A binary tree's height is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        #write a function to get the height
        def height_calculator(node):
            #base case
            if not node:
                return 0
            #get the height on the left and right arm
            left=height_calculator(node.left)
            right=height_calculator(node.right)
            #link left and right with the present
            return 1+max(left,right)
        
        #get the answer
        height=height_calculator(A)

        #return the answer
        return height
