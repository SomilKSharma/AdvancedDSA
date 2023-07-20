'''
Given a Binary Search Tree A. Check whether there exists a node 
with value B in the BST.
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
    # @return an integer
    def solve(self, A, B):

        #iterate through the binary Search tree
        def search_value(node):
            #check the base
            if not node:
                return False
            #check for the present node
            if node.val==B:
                return True
            #check for other values
            elif node.val<B:
                return search_value(node.right)
            else:
                return search_value(node.left)
        
        #call the function
        answer=search_value(A)

        #return answer to integer
        return int(answer)
