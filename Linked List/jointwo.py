'''Merge two sorted linked lists, A and B, and return it as a new list.
The new list should be made by splicing together the nodes of the first 
two lists and should also be sorted.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):

        #create the head from the minimum
        if A.val<B.val:
            head=A
            A=A.next
        else:
            head=B
            B=B.next
        
        #get head reference
        node=head
        #iterate for the rest of the values
        while A and B:
            #link to the next minimum element
            if A.val<B.val:
                node.next=A
                A=A.next
            else:
                node.next=B
                B=B.next
            #iterate to the next node
            node=node.next
        
        #iterate for the remaining element
        if A:
            node.next=A
        elif B:
            node.next=B
        
        #return the sorted linked list
        return head
