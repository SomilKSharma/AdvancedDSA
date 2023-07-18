'''
You are given the head of a linked list A and an integer B. You need to find the B-th element of the linked list.

Note : Follow 0-based indexing for the node numbering.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get a position variable
        pos=0

        #get a node reference
        node=A

        #iterate till both the conditions are true
        while node and pos!=B:
            #iterate to the next node
            node=node.next
            #iterate with the next position
            pos=pos+1
        
        #check for node or pos
        if not node:
            return None
        else:
            return node.val
