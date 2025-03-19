
# fib1=0
# fib2=1
# total=0
# n=11
# for i in range(1,n):
#     total=fib1+fib2
#     print(total)
#     fib1=fib2
#     fib2=total

class Solution:
    def fib(self, n: int) -> int:
        
        if(n<=1):
            return n
        
        return self.fib((n)-1)+self.fib((n)-2)
        
sol=Solution()

print(sol.fib(30))
        


    