'''
You are given a string A of size N consisting of lowercase alphabets.
You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
Find the minimum number of distinct characters in the resulting string.
'''
class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get a freq array
        array=[0]*26
        for value in A:
            array[ord(value)-97]+=1
        
        #sort the array
        array.sort()

        #counter variable
        counter=0

        #iterate till B
        index=0
        while B and index<26:
            #check if A[index] can be deducted, to reduce unique
            if array[index]<=B:
                B=B-array[index]
                array[index]=0
            #iterate to the next element
            index=index+1
        
        #count the unique elements
        count=0
        for value in array:
            #iterate count
            if value>0:
                count+=1
        
        #return the count
        return count if count else 1
        


