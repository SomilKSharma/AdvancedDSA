'''
Given an array where elements are sorted in ascending order, 
convert it to a height Balanced Binary Search Tree (BBST).
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):

        #write a function to create the binary search tree
        def construction(start,end):
            #base case
            if start>end:
                return None
            #find the middle point
            mid=(start+end)//2
            #create the node
            node=TreeNode(A[mid])
            #give the left and the right nodes
            node.left=construction(start,mid-1)
            node.right=construction(mid+1,end)
            #return the node
            return node
        
        #get the root of the node
        root=construction(0,len(A)-1)

        #return the root
        return root
