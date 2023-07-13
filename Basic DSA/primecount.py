#You need to return the count of prime numbers less than or equal to n.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #take a prime counter
        prime=0

        #iterate for the range
        for number in range(A+1):
            #edge cases
            if number<2:
                continue
            #else count the factors
            counter=0
            fact=1
            while fact*fact<=number:
                if number%fact==0:
                    counter+=2
                fact=fact+1
            
            #check for prime
            if counter>2:
                pass
            else:
                prime+=1
        
        #return the prime value
        return prime

