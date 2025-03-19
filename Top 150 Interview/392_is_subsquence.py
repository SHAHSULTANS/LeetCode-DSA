

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ctn=0
        
        for i in range(len(t)):
            if ctn<len(s) and s[ctn]==t[i]:
                ctn+=1

        return ctn==len(s)
    
s = "abc"
t = "ahbgdc"
ob=Solution()
print(ob.isSubsequence(s,t))