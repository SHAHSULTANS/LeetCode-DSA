class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sarray=s.split()
        ans=sarray[len(sarray)-1]
        return len(ans)
        
        
s = "   fly me   to   the moon  "
ob=Solution()
ob.lengthOfLastWord(s)