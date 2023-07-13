#Your task is to find all the common elements in both the array.
# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.

        #create a hashmap out of A
        hashmap={}
        for value in A:
            hashmap[value]=hashmap.get(value,0)+1

        #get an answer array
        answer=[]

        #iterate through all the values in B
        for value in B:
            #check for freq in hashmap
            if value in hashmap:
                answer.append(value)
                #check for freq
                hashmap[value]=hashmap[value]-1
                #delete the value if 0
                if hashmap[value]==0:
                    del hashmap[value]  

        #result the answer
        return answer 
