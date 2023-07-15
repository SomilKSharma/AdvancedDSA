#return the Ath ibonacci Number using recursion.
class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):

        #write a recursive code
        def fibonacci(term):
            #base case
            if term in [0,1]:
                return term
            #else calculate the value
            answer=fibonacci(term-1)+fibonacci(term-2)
            #return the answer
            return answer
        
        #return the value
        return fibonacci(A)
