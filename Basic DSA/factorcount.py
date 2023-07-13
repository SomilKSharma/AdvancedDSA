#Given an integer A, you need to find the count of it's factors.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #counter variable
        counter=0

        #iterate to the square root to get the answer
        fact=1
        sqrt=A**0.5
        while fact*fact<=A:
            #check if the fact divides A
            if not A%fact:
                counter+=2
            #increment fact
            fact=fact+1
        
        #check if prefect square of A exists
        if int(sqrt)==sqrt:
            return counter-1
        else:
            return counter

