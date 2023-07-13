'''
Groot has N trees lined up in front of him where the height of the i'th tree is denoted by H[i].

He wants to select some trees to replace his broken branches.

But he wants uniformity in his selection of trees.

So he picks only those trees whose heights have frequency B.

He then sums up the heights that occur B times. (He adds the height only once to the sum and not B times).
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, A, B, C):

        #create a hashmap out of C
        hashmap={}
        for value in C:
            hashmap[value]=hashmap.get(value,0)+1
        
        #get the answer
        answer=0
        found=False

        #check for all elements and add those with freq
        for key,freq in hashmap.items():
            if freq==B:
                answer=answer+key
                found=True
        
        return answer%1000000007 if found else -1
