


class Solution:
    def reverseWords(self, s: str) -> str:
        copylist=(s.split())
        n=len(copylist)
        ans=""
        firt_time=0
        
        for i in range(n-1,-1,-1):
            if(len(copylist[i]) and firt_time==0):
                ans+=copylist[i]
                firt_time=1
            elif len(copylist[i]):
                ans+=" "+copylist[i]
                
        return ans
        
        
        
s = "  hello world   "
ob=Solution()
print(ob.reverseWords(s))        