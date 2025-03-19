class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=y=str(x)
        y=y[::-1]
        if(y==x):
            return True
        
        return False
        
        

s="shanto"
s=s[::-1]
print(s)