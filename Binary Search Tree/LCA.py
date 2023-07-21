'''
Find the lowest common ancestor in an unordered binary tree A, 
given two values, B and C, in the tree.

Lowest common ancestor: the lowest common ancestor (LCA) of two 
nodes and w in a tree or directed acyclic graph (DAG) is the 
lowest (i.e., deepest) node that has both v and w as descendants.
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
	# @param C : integer
	# @return an integer
	def lca(self, A, B, C):

        #arrays for path of B and C
        path_b=[]
        path_c=[]

        #write a function to get path of a node in a tree
        def paths_to_node_b(node):
            #base case of the recursion
            if not node:
                return False
            #elif the value is found
            if node.val==B:
                path_b.append(node.val)
                return True
            #else check for both left and right in the node
            left_bool=paths_to_node_b(node.left)
            right_bool=paths_to_node_b(node.right)
            #check for both and return
            if left_bool or right_bool:
                path_b.append(node.val)
                return True
            else:
                return False
        
        #write a function to get path of a node in a tree
        def paths_to_node_c(node):
            #base case of the recursion
            if not node:
                return False
            #elif the value is found
            if node.val==C:
                path_c.append(node.val)
                return True
            #else check for both left and right in the node
            left_bool=paths_to_node_c(node.left)
            right_bool=paths_to_node_c(node.right)
            #check for both and return
            if left_bool or right_bool:
                path_c.append(node.val)
                return True
            else:
                return False

        paths_to_node_b(A)
        paths_to_node_c(A)

        #edge cases of either being the LCA
        if B in path_c:
            return B
        elif C in path_b:
            return C
        
        path_b=path_b[::-1]
        path_c=path_c[::-1]
        #iterate for each value in the arrays path_b and path_c
        for index in range(min(len(path_c),len(path_b))):
            #check for both array values
            if path_b[index]!=path_c[index]:
                break
        
        return path_b[index-1] if (path_b and path_c) else -1

            
