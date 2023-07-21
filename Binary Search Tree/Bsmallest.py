'''
Given a binary search tree represented by root A, 
write a function to find the Bth smallest element in the tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):

        #get a counter to identify Bth item
        global counter
        global answer
        counter=0
        answer=0

        #write a function to preform inorder traversal
        def inorder(node):
            #global counter and answer variable
            global counter
            global answer
            #write the base case of the code
            if not node:
                return
            #go for the left(smallest elements)
            inorder(node.left)
            #upgrade the counter for the node at present
            counter=counter+1
            #check if the answer is found
            if counter==B:
                answer=node.val
            #call the right elements
            inorder(node.right)
        
        #get the answer from the function call
        inorder(A)

        #return the answer
        return answer 