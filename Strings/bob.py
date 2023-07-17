'''
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        #get a counter variable
        counter=0

        #check for each index
        for index in range(len(A)-2):
            #check if 'bob' is found
            if A[index:index+3]=='bob':
                counter+=1
        
        #return the counter
        return counter
