'''
Implement a First In First Out (FIFO) queue using stacks only.

The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the UserQueue class:

void push(int X) : Pushes element X to the back of the queue.
int pop() : Removes the element from the front of the queue and returns it.
int peek() : Returns the element at the front of the queue.
boolean empty() : Returns true if the queue is empty, false otherwise.
NOTES:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
'''
from collections import deque
class UserQueue:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1=deque()
        self.stack_2=deque()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #check for the stacks are empty or not
        if not self.stack_1 and not self.stack_2:
            return -1
        #if only stack_2 is empty, fill it
        elif not self.stack_2:
            #while stack_1 exists
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        #return the top of stack_2
        return self.stack_2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        #check for the stacks are empty or not
        if not self.stack_1 and not self.stack_2:
            return -1
        #if only stack_2 is empty, fill it
        elif not self.stack_2:
            #while stack_1 exists
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        #return the top of stack_2
        return self.stack_2[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        #check for the stacks are empty or not
        if not self.stack_1 and not self.stack_2:
            return True
        else:
            return False

# Your UserQueue object will be instantiated and called as such:
# obj = UserQueue()
# obj.push(x)
# param2 = obj.pop()
# param3 = obj.peek()
# param4 = obj.empty()