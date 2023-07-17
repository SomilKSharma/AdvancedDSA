'''
You are given the head of a linked list A and an integer B. Delete the B-th node from the linked list.
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
    # @return the head node in the linked list
    def solve(self, A, B):

        #edge case, if B is equal to zero
        if not B:
            return A.next
        
        #iterate till B-1 position is reached
        node=A
        pos=0
        while pos!=B-1:
            #iterate to the next node
            node=node.next
            pos=pos+1
        
        #Delete the node
        node.next=node.next.next

        #return the head
        return A