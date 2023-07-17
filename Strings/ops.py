'''
Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:

Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.

NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        A=A*2
        
        new_A=''
        for value in A:
            if value.isupper():
                pass
            else:
                new_A+=value
        
        new_new_A=''
        for value in new_A:
            if value in'aeiou':
                new_new_A+='#'
            else:
                new_new_A+=value
        
        return new_new_A