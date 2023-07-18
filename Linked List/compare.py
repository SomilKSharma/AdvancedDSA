'''Given heads of two linked lists A and B, check if they are 
identical i.e. each of their corresponding nodes should contain 
the same data. The two given linked lists may or may not be of the 
same length.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return an integer
    def solve(self, A, B):

        #take reference of the node
        node_a,node_b=A,B

        #iterate for the nodes
        while node_a and node_b:
            #check for equality
            if node_a.val!=node_b.val:
                return 0
            #iterate to the next node
            node_a,node_b=node_a.next,node_b.next
        
        #check if n=both linked lists are exhausted
        if not node_a and not node_b:
            return 1
        else:
            return 0