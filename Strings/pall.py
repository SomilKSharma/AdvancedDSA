'''
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).
'''
sys.setrecursionlimit(10**8)
class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):

        #write a function to get the longth of the present substring
        def pallindrome(start,end):
            #base case
            if start<0 or end>=len(A):
                return 0
            #check if equal
            if A[start]==A[end]:
                #assume the code works for middle string
                length=pallindrome(start-1,end+1)
                #link middle with present
                return length+2
            else:
                return 0
        
        #get a maxi variable and answer variable
        maxi=0
        answer=''

        #iterate using two pointers
        start=end=0
        while end<len(A):
            #pointers in the same position
            if start==end:
                length=pallindrome(start-1,end+1)+1
                #check for maxi
                if maxi<length:
                    maxi=length
                    answer=A[start-length//2:end+length//2+1]
                end=end+1
            #end is one ahead of the start
            else:
                length=pallindrome(start,end)
                #check for maxi
                if maxi<length:
                    maxi=length
                    answer=A[start-length//2+1:end+length//2]
                start=start+1
        
        #return the answer
        return answer
