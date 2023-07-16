#Sort the given array in increasing order of number of distinct factors of each element
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #get a modified sorting function
        def sorting(number):
            #count the factors
            count=0
            fact=1
            while fact*fact<=number:
                #check if divisible
                if number%fact==0:
                    count=count+2
                fact=fact+1
            #edge case
            if number**0.5==int(number**0.5):
                count=count-1
            #return the value
            return count,number
        
        #use the modfies sorting function to get the answer
        A.sort(key=sorting)

        #return the value
        return A
                    
