'''
Write a program to find the node at which the intersection of two singly linked lists, A and B, begins. For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

Definition for singly-linked list
class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None
'''
class Solution:
    def getIntersectionNode(self, A, B):

        #edge case
        if not A or not B:
            return None

        #check if there is an intersection and get length of each
        length_a=1
        last_a=A
        while last_a.next:
            length_a=length_a+1
            last_a=last_a.next
        
        length_b=1
        last_b=B
        while last_b.next:
            length_b=length_b+1
            last_b=last_b.next
        
        #if the two don't intersect
        if last_a!=last_b:
            return None
        
        #check which length is greater
        difference=abs(length_a-length_b)
        if length_a>length_b:
            #iterate for the difference
            for _ in range(difference):
                A=A.next
        else:
            #iterate for the difference
            for _ in range(difference):
                B=B.next
        
        #iterate both till we reach the intersection
        while A!=B:
            A=A.next
            B=B.next
        
        #return the intersection point
        return A


        