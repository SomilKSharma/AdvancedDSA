'''
Given a linked list A, swap every two adjacent nodes and return its head.
NOTE: Your algorithm should use only constant space. You may not modify the 
values in the list; only nodes themselves can be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):

        #edge case of one element
        if not A.next:
            return A

        #add a dummy node in front of the head
        dummy=ListNode(None)
        dummy.next=A
        A=dummy

        #get the reference to the node
        node=A

        #swap the adjacent nodes
        prev=node
        curr=node.next

        #iterate through the Linked list
        while curr and curr.next:
            #inverse the adjacent elements
            prev.next=curr.next
            curr.next=prev.next.next
            prev.next.next=curr
            #iterate to the next node
            prev=curr
            curr=curr.next
        
        #return the new linked list
        return A.next


