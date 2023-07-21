'''
Given a binary tree. Check whether the given tree is a Sum-binary 
Tree or not. Sum-binary Tree is a Binary Tree where the value of a 
every node is equal to sum of the nodes present in its left subtree 
and right subtree.

An empty tree is Sum-binary Tree and sum of an empty tree can be 
considered as 0. A leaf node is also considered as SumTree.
Return 1 if it sum-binary tree else return 0.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        #write function to check if the bst is a sum bst
        def sum_bst(node):
            #base case
            if not node:
                return 0,True
            #check sum bst for left node
            left_sum,left_bst=sum_bst(node.left)
            #check sum bst for right node
            right_sum,right_bst=sum_bst(node.right)
            #check for the left and the right nodes
            if not left_bst or not right_bst:
                return 0,False
            else:
                #when the node is a leaf node
                if not node.left and not node.right:
                    return node.val,True
                #for all other cases
                elif node.val==left_sum+right_sum:
                    return node.val*2,True
                else:
                    return 0,False
        
        #answer of the tree
        _,answer=sum_bst(A)

        #return the int value of the answer
        return int(answer)
                
                
