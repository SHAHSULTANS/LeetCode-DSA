class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        self.n=(n)
        if(self.n==0):
            return False
        if(self.n==1):
            return True
        if(n%2==0):
            return True and self.isPowerOfTwo(n/2)
        else:
            return False and self.isPowerOfTwo(n/2)
            
obj=Solution()
print(obj.isPowerOfTwo(32))