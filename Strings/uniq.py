'''
Given a string A, find the length of the longest substring without repeating characters.

Note: Users are expected to solve in O(N) time complexity.
'''
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):

        #create a hashset
        hashset=set()

        #get maxi
        maxi=0

        #iterate for each value of A
        start=end=0
        while end<len(A):
            #check if the given value is in the array A
            while A[end] in hashset:
                hashset.remove(A[start])
                start=start+1
            #add A[end] to set
            hashset.add(A[end])
            #get the length and compare with maxi
            maxi=max(
                maxi,
                end-start+1
            )
            #iterate the end
            end=end+1
        
        #return the maxi
        return maxi

        
