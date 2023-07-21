'''
Given a Binary Search Tree A. Also given are two nodes B and C. 
Find the lowest common ancestor of the two nodes.

Note 1 :- It is guaranteed that the nodes B and C exist.

Note 2 :- The LCA of B and C in A is the shared ancestor of B 
and C that is located farthest from the root.
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
                return node.val
            #else iterate to the either sides
            elif node.val<=min(B,C):
                return bst_lca(node.right)
            else:
                return bst_lca(node.left)
        
        #get the answer
        answer=bst_lca(A)

        #return the answer
        return answer


                
            