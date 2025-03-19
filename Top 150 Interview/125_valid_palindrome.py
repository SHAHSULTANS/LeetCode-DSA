
import string

from pyparsing import alphanums

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        after_removing="".join(x.lower() for x in s if x.isalnum())
        return after_removing==after_removing[::-1]
        # lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        # alphabet=[]
        # for char in s:
        #     if char.lower() in lowercase_letters:
        #         alphabet.append(char.lower())
                
                
        # i,j=0,len(alphabet)-1
        # while i<j:
        #     if alphabet[i]!=alphabet[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True
                
                
s="sha?: N"
ob=Solution()
ob.isPalindrome(s)
print( alphanums)
