'''
A CPU has N tasks to be performed. 
It is to be noted that the tasks have to be completed in a 
specific order to avoid deadlock. In every clock cycle, the 
CPU can either perform a task or move it to the back of the 
queue. You are given the current state of the scheduler queue 
in array A and the required order of the tasks in array B. 

Determine the minimum number of clock cycles to complete all the tasks.
'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        #use the arrays as queues for gettin the answer
        #get a value variable to store the value
        cycles=0
        #while all the tasks aren't done
        while A:
            #check for equality
            while A[0]!=B[0]:
                #remove task from first and add at the last
                A.append(A.pop(0))
                #increment the counter
                cycles+=1
            A.pop(0)
            B.pop(0)
            cycles+=1
        
        #return the cycles
        return cycles
            

