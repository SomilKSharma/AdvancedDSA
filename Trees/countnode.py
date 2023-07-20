'''
You are given the root node of a binary tree A. 
You have to find the number of nodes in this tree.
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

        #write function to count the number of nodes
        def node_counter(node):
            #base case
            if not node:
                return 0
            #assume code works for left and right
            left_count=node_counter(node.left)
            right_count=node_counter(node.right)
            #connect left and right with the present node
            return 1+left_count+right_count
        
        #get the node count
        count=node_counter(A)

        #return the value
        return count
