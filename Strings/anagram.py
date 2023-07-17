'''
You are given two strings, A and B, of size N and M, respectively.

You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        #create a hashmap if A
        hashmap_a={}
        for value in A:
            hashmap_a[value]=hashmap_a.get(value,0)+1

        #get the length of A
        length=len(A)

        #iterate for first window of length in B
        hashmap_b={}
        for index in range(length):
            hashmap_b[B[index]]=hashmap_b.get(B[index],0)+1
        
        #get a counter
        counter=0
        if hashmap_a==hashmap_b:
            counter+=1
        
        #slide the window
        for index in range(len(B)-length):
            #remove B[index]
            if hashmap_b[B[index]]==1:
                del hashmap_b[B[index]]
            else:
                hashmap_b[B[index]]=hashmap_b[B[index]]-1
            #add B[index+length]
            hashmap_b[B[index+length]]=hashmap_b.get(B[index+length],0)+1
            #compare the two
            if hashmap_a==hashmap_b:
                counter+=1
        
        #return the value
        return counter