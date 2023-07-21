'''
Given a binary tree A. Check whether it is possible to partition 
the tree to two trees which have equal sum of values after removing 
exactly one edge on the original tree.
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

        #create a hashset to store values
        hashset=set()

        #call teh function to store values of all values/sums
        def find_all_sums(node):
            #base case for the recursive code for either sides of the tree
            #left side
            if node.left:
                left_sum=find_all_sums(node.left)
            else:
                left_sum=0
            #right side
            if node.right:
                right_sum=find_all_sums(node.right)
            else:
                right_sum=0
            #add the values to the hashset
            hashset.add(node.val)
            hashset.add(node.val+left_sum+right_sum)
            #return the sum till this point
            return node.val+left_sum+right_sum
        
        #get the final sum
        final=find_all_sums(A)

        #Check for divisbility of sum
        if final&1:
            return 0
        else:
            #check if half of sum is in the hashset
            if final//2 in hashset:
                return 1
            else:
                return 0
        