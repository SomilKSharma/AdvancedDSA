'''
Given a linked list of integers, find and return the middle element of the linked list.
NOTE: If there are N nodes in the linked list and N is even then 
return the (N/2 + 1)th element.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):

        #get the slow and faster pointer
        slow=fast=A

        #iterate till fast pointere reaches the end
        while fast and fast.next:
            #iterate the slower one
            slow=slow.next
            #iterate the fast pointer
            fast=fast.next.next
        
        #return the slow pointer
        return slow.val
