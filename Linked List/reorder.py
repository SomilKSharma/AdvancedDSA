'''Given a singly linked list A

A: A0 → A1 → … → An-1 → An 
reorder it to:
A0 → An → A1 → An-1 → A2 → An-2 → … 

You must do this in-place without altering the nodes' values.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):

        #write a function to reverse the linked list
        def reverse(node):
            #previous,current and the future pointer is needed
            prev=None
            curr=node
            later=node.next

            #iterate and reverse
            while curr:
                curr.next=prev
                prev=curr
                curr=later
                if later:
                    later=later.next
            
            #return the new head
            return prev
        
        #get a slow and a fast pointer to get the middle pointer
        slow=fast=A
        while fast and fast.next:
            #iterate the slow pointer
            slow=slow.next
            #iterate the fast pointer
            fast=fast.next.next
        
        #reverse the elements after slow pointer

        #edge case of linked list with one length
        if not slow.next:
            return A
        
        #call the reverse function
        head=reverse(slow.next)
        slow.next=None

        #merge the old and new linked list recursively
        node=A
        while head:
            #merget the two
            later_left=node.next
            node.next=head
            later_right=head.next
            head.next=later_left
            node=later_left
            head=later_right

        #return the answer
        return A


