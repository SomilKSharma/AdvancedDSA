#tower of Hanoi
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):

        #get an answer array
        answer=[]

        #write the recursive code
        def hanoi_solution(A,start,end):
            #check for base case
            if not A:
                return
            #assume code has moved n-1 to the mid position
            hanoi_solution(A-1,start,6-start-end)
            #move end to the end position
            answer.append([A,start,end])
            #assume the code moves n-1 to the end position
            hanoi_solution(A-1,6-start-end,end)
        
        #call the function
        hanoi_solution(A,1,3)

        #return the answer
        return answer

