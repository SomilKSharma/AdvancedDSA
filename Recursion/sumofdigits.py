#sum of digits
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #recursive function to get the answer
        def sum_of_digits(number):
            #base case
            if not number:
                return 0
            #assume that rest of the digits have been sumned up
            sums=sum_of_digits(number//10)
            #link rest witht the present digit
            return sums+number%10
        
        #return the answer
        return sum_of_digits(A)
