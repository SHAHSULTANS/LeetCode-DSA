class Solution:
    def calculate(self,base,exp):
        if exp==0:
            return 1
        
        return base* self.calculate(base,exp-1)
        
        
    def myPow(self, x: float, n: int) -> float:
        # print(n)
        result=self.calculate(x,abs(n))
        # print(n)
        if(n<0):
            result=1/result
        return f"{result:.5f}"
        
# print(1)
ob=Solution()

print(ob.myPow(0.00001,2147483647))

        