#Given an integer A, generate a square matrix filled with elements from 1 to A2
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):

        #edge case
        if A==1:
            return [[1]]
        
        #get the answer array
        answer=[
            [0]*A
            for _ in range(A)
        ]

        #counter for the loop
        row=col=0
        number=1

        while A>1:
            #for loops for rows and cols
            for _ in range(A-1):
                answer[row][col]=number
                number+=1
                col=col+1
            #for loops for rows and cols
            for _ in range(A-1):
                answer[row][col]=number
                number+=1
                row=row+1
            #for loops for rows and cols
            for _ in range(A-1):
                answer[row][col]=number
                number+=1
                col=col-1
            #for loops for rows and cols
            for _ in range(A-1):
                answer[row][col]=number
                number+=1
                row=row-1

            #change values
            row=row+1
            col=col+1
            A=A-2
            if A==1:
                answer[row][col]=number
        
        return answer