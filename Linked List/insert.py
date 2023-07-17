'''
You are given A which is the head of a linked list. Also given is the value B and position C. Complete the function that should insert a new node with the said value at the given position.

Notes:

In case the position is more than length of linked list, simply insert the new node at the tail only.
In case the pos is 0, simply insert the new node at head only.
Follow 0-based indexing for the node numbering.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def solve(self, A, B, C):

        #create a new node
        new_node=ListNode(B)

        #edge case
        if not C:
            #make new the head
            new_node.next=A
            return new_node
        
        #iterate till last node or before the position to be inserted
        node_pos=0
        node=A
        while node.next and node_pos!=C-1:
            node=node.next
            node_pos=node_pos+1
        
        #insert node at the following node
        new_node.next=node.next
        node.next=new_node

        #return the original head
        return A
