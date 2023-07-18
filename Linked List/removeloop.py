'''You are given a linked list that contains a loop.
You need to find the node, which creates a loop and break it 
by making the node point to NULL.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):

        #create a slow and a fast pointer
        slow=fast=A
        #iterate both once
        slow=slow.next
        fast=fast.next.next
        #iterate till not equal
        while slow!=fast:
            slow=slow.next
            fast=fast.next.next
        
        #get a start pointer
        start=A
        #iterate till start and slow become equal
        prev=None
        while slow!=start:
            #iterate
            prev=slow
            slow=slow.next
            start=start.next
        
        #make prev next to None to cut the loop
        prev.next=None

        #return the answer
        return A
