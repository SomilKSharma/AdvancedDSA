'''
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents the length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of the board.

Calculate and return the minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of the board.
NOTE: 
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.

Return the ans % 10000003.
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):

        #write a function to check if the max distance is working
        def checker(distance):
            #take a counter
            counter=1
            #take length painted
            length=0
            #iterate for each value in the array C
            for value in C:
                #new length
                length=length+value
                #check for limit
                if length>distance:
                    length=value
                    counter+=1
            #check if the following will work
            if counter<=A:
                return True
            else:
                return False
        
        #get an answer variable
        answer=0
        
        #write the binary search
        start,end=max(C),sum(C)
        while start<=end:
            #get the mid value in the array
            mid=(start+end)//2
            #check for mid validity
            if checker(mid):
                answer=mid
                end=mid-1
            else:
                start=mid+1
        
        #return the value
        return (answer*B)%10000003

