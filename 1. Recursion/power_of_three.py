class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        
        if(n==1):
            return True
        if(n%3):
            return False
        else:
            return self.isPowerOfThree(n/3)
        
        
        
        
ob=Solution()

print(ob.isPowerOfThree(31))