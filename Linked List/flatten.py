"""
Given a linked list where every node represents a linked list and contains two pointers of its type:

Pointer to right node in the main list (right pointer)
Pointer to a linked list where this node is head (down pointer). All linked lists are sorted.
You are asked to flatten the linked list into a single list. Use down pointer to link nodes of 
the flattened list. The flattened linked list should also be sorted.

class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None
"""
# @param root: ListNode
# @return ListNode
def flatten(root):

    #write a function to combine both the linked list
    def combine(node_a,node_b):

        #get the head of the node
        if node_a.val<node_b.val:
            head=node=node_a
            node_a=node_a.down
        else:
            head=node=node_b
            node_b=node_b.down
        
        #itereate for the remaining nodes
        while node_a and node_b:
            #get the link to the node
            if node_a.val<node_b.val:
                node.down=node_a
                node_a=node_a.down
            else:
                node.down=node_b
                node_b=node_b.down
            #itereate to the down node
            node=node.down
        
        #join the remaining node
        if node_a:
            node.down=node_a
        else:
            node.down=node_b
        
        #return the head
        return head
    
    #iterate for all the nodes
    head=root
    while root.right:
        #further link
        link=root.right.right
        #get the new root
        first=root
        second=root.right
        #delink these nodes
        first.right=second.right=None
        #new root
        root=combine(first,second)
        #join the root
        root.right=link
    
    return root
    

            



    
        
