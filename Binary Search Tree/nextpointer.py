'''
Given a binary tree,

Populate each next pointer to point to its next right node. If 
there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
Assume perfect binary tree.
'''

# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):

        #create a queue for the binary tree
        queue=deque()
        #add the root node to the queue
        queue.append(root)

        #take the prev to be None by default
        prev=None

        #iterate till the queue exists
        while queue:
            #iterate for the entire level together
            prev=None
            for _ in range(len(queue)):
                #pop the element of the level
                node=queue.popleft()
                #link previous to this node
                if prev:
                    prev.next=node
                #make node of the present as None by default
                node.next=None
                #change prev to present
                prev=node
                #add elements for the next nodes
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root

        
